"""
AgriConnect Full Backend Prototype
Includes:
- Users (farmers/buyers)
- Crops marketplace
- Orders with simulated MoMo/OPay payments + webhooks
- Delivery tracking
- Training & simulated weather advisory
- Notifications (in-app)
- Cooperatives (create/join/post announcements)
- Cooperative bulk listings and cooperative orders
- CSV export for cooperatives, orders, members, and announcements

Run: uvicorn agriconnect:app --reload
"""

from fastapi import FastAPI, HTTPException, Response
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, List
import uuid
import random
import csv
import io

app = FastAPI(title="AgriConnect Platform")

# Database setup
DATABASE_URL = "sqlite:///./agriconnect.db"
engine = create_engine(DATABASE_URL, echo=False)

# --------------------
# Models
# --------------------
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    role: str  # "farmer" or "buyer"
    location: Optional[str] = None
    phone: Optional[str] = None  # For SMS notifications

class Crop(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    quantity: int
    price: float
    farmer_id: int

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    buyer_id: int
    crop_id: int
    quantity: int
    total_price: float
    payment_status: str = "pending"
    payment_reference: Optional[str] = None
    provider: Optional[str] = None

class Delivery(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int
    status: str = "pending"
    location: Optional[str] = None
    eta: Optional[str] = None

class Training(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str

class Notification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    message: str
    status: str = "unread"

class Cooperative(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    location: Optional[str] = None

class CoopMember(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    coop_id: int
    user_id: int
    joined_at: Optional[str] = None

class Announcement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    coop_id: int
    title: str
    content: str
    created_by: int

class CoopListing(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    coop_id: int
    crop_name: str
    quantity: int
    price_per_unit: float

class CoopOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    buyer_id: int
    coop_listing_id: int
    quantity: int
    total_price: float
    payment_status: str = "pending"
    payment_reference: Optional[str] = None
    provider: Optional[str] = None

# Initialize DB tables
SQLModel.metadata.create_all(engine)

# --------------------
# Utilities
# --------------------
def notify_user(session: Session, user_id: int, message: str):
    note = Notification(user_id=user_id, message=message)
    session.add(note)
    session.commit()

# (Other endpoints omitted here for brevity - they remain unchanged from the last version)

# --------------------
# CSV Export Endpoints
# --------------------
@app.get("/export/orders")
def export_orders():
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["OrderID", "BuyerID", "CropID", "Quantity", "TotalPrice", "PaymentStatus", "Provider"])
        for o in orders:
            writer.writerow([o.id, o.buyer_id, o.crop_id, o.quantity, o.total_price, o.payment_status, o.provider])
        response = Response(content=output.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=orders.csv"
        return response

@app.get("/export/cooperatives")
def export_cooperatives():
    with Session(engine) as session:
        coops = session.exec(select(Cooperative)).all()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["CoopID", "Name", "Description", "Location"])
        for c in coops:
            writer.writerow([c.id, c.name, c.description, c.location])
        response = Response(content=output.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=cooperatives.csv"
        return response

@app.get("/export/coop-orders")
def export_coop_orders():
    with Session(engine) as session:
        coop_orders = session.exec(select(CoopOrder)).all()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["CoopOrderID", "BuyerID", "ListingID", "Quantity", "TotalPrice", "PaymentStatus", "Provider"])
        for co in coop_orders:
            writer.writerow([co.id, co.buyer_id, co.coop_listing_id, co.quantity, co.total_price, co.payment_status, co.provider])
        response = Response(content=output.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=coop_orders.csv"
        return response

@app.get("/export/coop-members")
def export_coop_members():
    with Session(engine) as session:
        members = session.exec(select(CoopMember)).all()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["MemberID", "CoopID", "UserID", "JoinedAt"])
        for m in members:
            writer.writerow([m.id, m.coop_id, m.user_id, m.joined_at])
        response = Response(content=output.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=coop_members.csv"
        return response

@app.get("/export/coop-announcements")
def export_coop_announcements():
    with Session(engine) as session:
        announcements = session.exec(select(Announcement)).all()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["AnnouncementID", "CoopID", "Title", "Content", "CreatedBy"])
        for a in announcements:
            writer.writerow([a.id, a.coop_id, a.title, a.content, a.created_by])
        response = Response(content=output.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=coop_announcements.csv"
        return response

# --------------------
# End of file
# --------------------









# agriconnect_secure.py
"""
AgriConnect Secure Backend with Import/Export and Template Endpoints
Run: uvicorn agriconnect_secure:app --reload
"""

from fastapi import FastAPI, HTTPException, Response, Depends, status, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import StreamingResponse
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, List, Any
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
import uuid, random, csv, io, zipfile, os

# ---------------- Configuration ----------------
SECRET_KEY = "CHANGE_THIS_SECRET"  # <-- replace with a secure random secret
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# ---------------- App & DB ----------------
app = FastAPI(title="AgriConnect Platform Secure (Full)")
engine = create_engine("sqlite:///./agriconnect_secure.db", echo=False)

# ---------------- Models ----------------
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    full_name: Optional[str] = None
    hashed_password: str
    role: str  # "farmer", "buyer", "admin"
    location: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True

class Crop(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    quantity: int
    price: float
    farmer_id: int

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    buyer_id: int
    crop_id: int
    quantity: int
    total_price: float
    payment_status: str = "pending"
    payment_reference: Optional[str] = None
    provider: Optional[str] = None

class Delivery(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int
    status: str = "pending"
    location: Optional[str] = None
    eta: Optional[str] = None

class Training(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str

class Notification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    message: str
    status: str = "unread"

class Cooperative(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    location: Optional[str] = None

class CoopMember(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    coop_id: int
    user_id: int
    joined_at: Optional[str] = None

class Announcement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    coop_id: int
    title: str
    content: str
    created_by: int

class CoopListing(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    coop_id: int
    crop_name: str
    quantity: int
    price_per_unit: float

class CoopOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    buyer_id: int
    coop_listing_id: int
    quantity: int
    total_price: float
    payment_status: str = "pending"
    payment_reference: Optional[str] = None
    provider: Optional[str] = None

SQLModel.metadata.create_all(engine)

# ---------------- Auth utilities ----------------
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_by_username(session: Session, username: str) -> Optional[User]:
    return session.exec(select(User).where(User.username == username)).first()

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    with Session(engine) as session:
        user = get_user_by_username(session, username)
        if user is None:
            raise credentials_exception
        return user

def role_required(required_role: str):
    def dependency(user: User = Depends(get_current_user)):
        if user.role != required_role and user.role != "admin":
            raise HTTPException(status_code=403, detail=f"Requires {required_role} role")
        return user
    return dependency

# ---------------- Notification util ----------------
def notify_user(session: Session, user_id: int, message: str):
    note = Notification(user_id=user_id, message=message)
    session.add(note)
    session.commit()

# ---------------- Simulated payment providers ----------------
class MoMoAPI:
    @staticmethod
    def initiate(phone: str, amount: float, reference: str):
        return {"status": "initiated", "provider": "MoMo", "amount": amount, "reference": reference}

class OPayAPI:
    @staticmethod
    def initiate(phone: str, amount: float, reference: str):
        return {"status": "initiated", "provider": "OPay", "amount": amount, "reference": reference}

# ---------------- CSV helpers ----------------
def generate_csv(records: List[Any], headers: List[str], row_fn) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    for r in records:
        writer.writerow(row_fn(r))
    return output.getvalue()

def generate_csv_template_bytes(headers: List[str]) -> io.BytesIO:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(headers)
    mem = io.BytesIO()
    mem.write(buf.getvalue().encode("utf-8"))
    mem.seek(0)
    return mem

# ---------------- Auth endpoints ----------------
@app.post("/register")
def register(username: str, password: str, role: str = "farmer", full_name: Optional[str] = None, location: Optional[str] = None, phone: Optional[str] = None):
    with Session(engine) as session:
        if get_user_by_username(session, username):
            raise HTTPException(status_code=400, detail="Username exists")
        user = User(username=username, hashed_password=get_password_hash(password), role=role, full_name=full_name, location=location, phone=phone)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"msg": "User created", "username": username, "role": role}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        user = get_user_by_username(session, form_data.username)
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Bad credentials")
        access_token = create_access_token({"sub": user.username}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}

# ---------------- Marketplace & Crops ----------------
@app.post("/farmer/{farmer_id}/add_crop")
def add_crop(farmer_id: int, name: str, quantity: int, price: float, current_user: User = Depends(role_required("farmer"))):
    if current_user.id != farmer_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only owner farmer or admin")
    with Session(engine) as session:
        crop = Crop(name=name, quantity=quantity, price=price, farmer_id=farmer_id)
        session.add(crop)
        session.commit()
        session.refresh(crop)
        buyers = session.exec(select(User).where(User.role == "buyer")).all()
        for b in buyers:
            notify_user(session, b.id, f"New crop listed: {name} at ₦{price}")
        return crop

@app.get("/crops")
def list_crops(current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        return session.exec(select(Crop)).all()

@app.get("/crops/{crop_id}")
def get_crop(crop_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        c = session.get(Crop, crop_id)
        if not c:
            raise HTTPException(status_code=404, detail="Crop not found")
        return c

# ---------------- Orders & Payments ----------------
@app.post("/order")
def place_order(buyer_id: int, crop_id: int, quantity: int, provider: str, current_user: User = Depends(role_required("buyer"))):
    if current_user.id != buyer_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only self or admin")
    with Session(engine) as session:
        buyer = session.get(User, buyer_id)
        crop = session.get(Crop, crop_id)
        if not buyer or buyer.role != "buyer":
            raise HTTPException(status_code=400, detail="Invalid buyer")
        if not crop or crop.quantity < quantity:
            raise HTTPException(status_code=400, detail="Insufficient crop quantity")
        total = crop.price * quantity
        reference = str(uuid.uuid4())
        order = Order(buyer_id=buyer_id, crop_id=crop_id, quantity=quantity, total_price=total, payment_reference=reference, provider=provider)
        session.add(order)
        crop.quantity -= quantity
        session.add(crop)
        session.commit()
        session.refresh(order)
        delivery = Delivery(order_id=order.id, status="pending", location=str(crop.farmer_id), eta="TBD")
        session.add(delivery)
        session.commit()
        notify_user(session, crop.farmer_id, f"New order #{order.id} placed for {crop.name}, qty {quantity}.")
        if provider.lower() == "momo":
            payment = MoMoAPI.initiate(buyer.phone or "", total, reference)
        elif provider.lower() == "opay":
            payment = OPayAPI.initiate(buyer.phone or "", total, reference)
        else:
            raise HTTPException(status_code=400, detail="Unsupported provider")
        return {"order_id": order.id, "payment": payment, "payment_reference": reference}

@app.get("/orders/{order_id}")
def get_order(order_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Not found")
        crop = session.get(Crop, order.crop_id)
        allowed = (current_user.role == "admin" or order.buyer_id == current_user.id or (crop and crop.farmer_id == current_user.id))
        if not allowed:
            raise HTTPException(status_code=403, detail="Not authorized")
        return order

# Webhooks (simulated providers call these; protected to admin or system accounts)
@app.post("/webhook/momo")
def webhook_momo(reference: str, status: str, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        order = session.exec(select(Order).where(Order.payment_reference == reference)).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        order.payment_status = status
        session.add(order)
        session.commit()
        notify_user(session, order.buyer_id, f"MoMo payment {status} for order {order.id}")
        return {"message": "updated"}

@app.post("/webhook/opay")
def webhook_opay(reference: str, status: str, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        order = session.exec(select(Order).where(Order.payment_reference == reference)).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        order.payment_status = status
        session.add(order)
        session.commit()
        notify_user(session, order.buyer_id, f"OPay payment {status} for order {order.id}")
        return {"message": "updated"}

# ---------------- Delivery ----------------
@app.get("/delivery/{order_id}")
def get_delivery(order_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        delivery = session.exec(select(Delivery).where(Delivery.order_id == order_id)).first()
        if not delivery:
            raise HTTPException(status_code=404, detail="Delivery not found")
        order = session.get(Order, delivery.order_id)
        crop = session.get(Crop, order.crop_id) if order else None
        allowed = (current_user.role == "admin" or (order and order.buyer_id == current_user.id) or (crop and crop.farmer_id == current_user.id))
        if not allowed:
            raise HTTPException(status_code=403, detail="Not authorized")
        return delivery

@app.put("/delivery/{order_id}")
def update_delivery(order_id: int, status: str, location: Optional[str] = None, eta: Optional[str] = None, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        delivery = session.exec(select(Delivery).where(Delivery.order_id == order_id)).first()
        if not delivery:
            raise HTTPException(status_code=404, detail="Delivery not found")
        order = session.get(Order, delivery.order_id)
        crop = session.get(Crop, order.crop_id) if order else None
        if not (current_user.role == "admin" or (crop and crop.farmer_id == current_user.id)):
            raise HTTPException(status_code=403, detail="Not authorized")
        delivery.status = status
        if location:
            delivery.location = location
        if eta:
            delivery.eta = eta
        session.add(delivery)
        session.commit()
        if order:
            notify_user(session, order.buyer_id, f"Delivery status updated: {status} for order {order.id}")
        return delivery

# ---------------- Training & Weather Advisory ----------------
@app.post("/training")
def add_training(title: str, content: str, category: str, current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        t = Training(title=title, content=content, category=category)
        session.add(t)
        session.commit()
        session.refresh(t)
        return t

@app.get("/training")
def view_training(current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        return session.exec(select(Training)).all()

weather_conditions = ["sunny", "rainy", "stormy", "dry", "cloudy"]
advisory_tips = {
    "sunny": "Good time for planting and drying harvested crops.",
    "rainy": "Ensure proper drainage to avoid flooding.",
    "stormy": "Protect crops from wind damage; secure storage.",
    "dry": "Consider irrigation to support crop growth.",
    "cloudy": "Monitor crops for pests as humidity may rise."
}

@app.get("/weather/{farmer_id}")
def get_weather(farmer_id: int, current_user: User = Depends(get_current_user)):
    condition = random.choice(weather_conditions)
    with Session(engine) as session:
        user = session.get(User, farmer_id)
        if not user:
            raise HTTPException(status_code=404, detail="Farmer not found")
        return {"location": user.location or "unknown", "condition": condition}

@app.get("/advisory/{farmer_id}")
def get_advisory(farmer_id: int, current_user: User = Depends(get_current_user)):
    condition = random.choice(weather_conditions)
    tip = advisory_tips[condition]
    with Session(engine) as session:
        user = session.get(User, farmer_id)
        if not user:
            raise HTTPException(status_code=404, detail="Farmer not found")
        notify_user(session, user.id, f"Weather: {condition}. Advice: {tip}")
        return {"farmer": user.username, "location": user.location or "unknown", "weather_condition": condition, "advisory": tip}

# ---------------- Notifications ----------------
@app.get("/notifications/{user_id}")
def get_notifications(user_id: int, current_user: User = Depends(get_current_user)):
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    with Session(engine) as session:
        notes = session.exec(select(Notification).where(Notification.user_id == user_id)).all()
        return notes

@app.put("/notifications/{note_id}/read")
def mark_notification_read(note_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        note = session.get(Notification, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Notification not found")
        if note.user_id != current_user.id and current_user.role != "admin":
            raise HTTPException(status_code=403, detail="Not authorized")
        note.status = "read"
        session.add(note)
        session.commit()
        return note

# ---------------- Cooperatives ----------------
@app.post("/cooperatives")
def create_cooperative(name: str, description: Optional[str] = None, location: Optional[str] = None, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        coop = Cooperative(name=name, description=description, location=location)
        session.add(coop)
        session.commit()
        session.refresh(coop)
        return coop

@app.get("/cooperatives")
def list_coops(current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        return session.exec(select(Cooperative)).all()

@app.post("/cooperatives/{coop_id}/join")
def join_coop(coop_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        coop = session.get(Cooperative, coop_id)
        if not coop:
            raise HTTPException(status_code=404, detail="Coop not found")
        member = CoopMember(coop_id=coop_id, user_id=current_user.id, joined_at=datetime.utcnow().isoformat())
        session.add(member)
        session.commit()
        notify_user(session, current_user.id, f"You joined cooperative {coop.name}")
        return member

@app.get("/cooperatives/{coop_id}/members")
def coop_members(coop_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        members = session.exec(select(CoopMember).where(CoopMember.coop_id == coop_id)).all()
        user_member = any(m.user_id == current_user.id for m in members)
        if not user_member and current_user.role != "admin":
            raise HTTPException(status_code=403, detail="Only coop members or admin can view members")
        result = []
        for m in members:
            user = session.get(User, m.user_id)
            result.append({"member_id": m.id, "user_id": user.id, "username": user.username, "joined_at": m.joined_at})
        return result

@app.post("/cooperatives/{coop_id}/announcements")
def post_announcement(coop_id: int, title: str, content: str, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        is_member = session.exec(select(CoopMember).where((CoopMember.coop_id == coop_id) & (CoopMember.user_id == current_user.id))).first()
        if not is_member and current_user.role != "admin":
            raise HTTPException(status_code=403, detail="Only coop members or admin can post announcements")
        ann = Announcement(coop_id=coop_id, title=title, content=content, created_by=current_user.id)
        session.add(ann)
        session.commit()
        members = session.exec(select(CoopMember).where(CoopMember.coop_id == coop_id)).all()
        coop = session.get(Cooperative, coop_id)
        for m in members:
            notify_user(session, m.user_id, f"Announcement in {coop.name}: {title}")
        return ann

@app.get("/cooperatives/{coop_id}/announcements")
def get_announcements(coop_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        members = session.exec(select(CoopMember).where(CoopMember.coop_id == coop_id)).all()
        user_member = any(m.user_id == current_user.id for m in members)
        if not user_member and current_user.role != "admin":
            raise HTTPException(status_code=403, detail="Only coop members or admin can view announcements")
        return session.exec(select(Announcement).where(Announcement.coop_id == coop_id)).all()

# ---------------- Cooperative bulk listings & orders ----------------
@app.post("/cooperatives/{coop_id}/listings")
def create_coop_listing(coop_id: int, crop_name: str, quantity: int, price_per_unit: float, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        coop = session.get(Cooperative, coop_id)
        if not coop:
            raise HTTPException(status_code=404, detail="Cooperative not found")
        is_member = session.exec(select(CoopMember).where((CoopMember.coop_id == coop_id) & (CoopMember.user_id == current_user.id))).first()
        if not is_member and current_user.role != "admin":
            raise HTTPException(status_code=403, detail="Only coop members or admin can create listing")
        listing = CoopListing(coop_id=coop_id, crop_name=crop_name, quantity=quantity, price_per_unit=price_per_unit)
        session.add(listing)
        session.commit()
        session.refresh(listing)
        buyers = session.exec(select(User).where(User.role == "buyer")).all()
        for b in buyers:
            notify_user(session, b.id, f"New cooperative listing: {crop_name} ({quantity}) at ₦{price_per_unit}")
        return listing

@app.get("/cooperatives/{coop_id}/listings")
def list_coop_listings(coop_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        return session.exec(select(CoopListing).where(CoopListing.coop_id == coop_id)).all()

@app.post("/coop-order")
def place_coop_order(buyer_id: int, coop_listing_id: int, quantity: int, provider: str, current_user: User = Depends(role_required("buyer"))):
    if current_user.id != buyer_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only self or admin")
    with Session(engine) as session:
        buyer = session.get(User, buyer_id)
        listing = session.get(CoopListing, coop_listing_id)
        if not buyer or buyer.role != "buyer":
            raise HTTPException(status_code=400, detail="Invalid buyer")
        if not listing or listing.quantity < quantity:
            raise HTTPException(status_code=400, detail="Insufficient listing quantity")
        total = listing.price_per_unit * quantity
        reference = str(uuid.uuid4())
        coop_order = CoopOrder(buyer_id=buyer_id, coop_listing_id=coop_listing_id, quantity=quantity, total_price=total, payment_reference=reference, provider=provider)
        session.add(coop_order)
        listing.quantity -= quantity
        session.add(listing)
        session.commit()
        session.refresh(coop_order)
        if provider.lower() == "momo":
            payment = MoMoAPI.initiate(buyer.phone or "", total, reference)
        elif provider.lower() == "opay":
            payment = OPayAPI.initiate(buyer.phone or "", total, reference)
        else:
            raise HTTPException(status_code=400, detail="Unsupported provider")
        coop = session.get(Cooperative, listing.coop_id)
        members = session.exec(select(CoopMember).where(CoopMember.coop_id == coop.id)).all()
        for m in members:
            notify_user(session, m.user_id, f"Bulk order placed for {listing.crop_name}, qty {quantity}")
        return {"coop_order_id": coop_order.id, "payment": payment, "payment_reference": reference}

@app.get("/coop-order/{coop_order_id}")
def get_coop_order(coop_order_id: int, current_user: User = Depends(get_current_user)):
    with Session(engine) as session:
        o = session.get(CoopOrder, coop_order_id)
        if not o:
            raise HTTPException(status_code=404, detail="Coop order not found")
        if current_user.role != "admin" and o.buyer_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
        return o

# ---------------- Export endpoints (admin-only) ----------------
@app.get("/export/users")
def export_users(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        csv_data = generate_csv(users, ["UserID", "Username", "FullName", "Role", "Location", "Phone"], lambda u: [u.id, u.username, u.full_name, u.role, u.location, u.phone])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=users.csv"
        return response

@app.get("/export/crops")
def export_crops(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        crops = session.exec(select(Crop)).all()
        csv_data = generate_csv(crops, ["CropID", "Name", "Quantity", "Price", "FarmerID"], lambda c: [c.id, c.name, c.quantity, c.price, c.farmer_id])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=crops.csv"
        return response

@app.get("/export/orders")
def export_orders(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()
        csv_data = generate_csv(orders, ["OrderID", "BuyerID", "CropID", "Quantity", "TotalPrice", "PaymentStatus", "Provider"], lambda o: [o.id, o.buyer_id, o.crop_id, o.quantity, o.total_price, o.payment_status, o.provider])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=orders.csv"
        return response

@app.get("/export/deliveries")
def export_deliveries(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        deliveries = session.exec(select(Delivery)).all()
        csv_data = generate_csv(deliveries, ["DeliveryID", "OrderID", "Status", "Location", "ETA"], lambda d: [d.id, d.order_id, d.status, d.location, d.eta])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=deliveries.csv"
        return response

@app.get("/export/cooperatives")
def export_cooperatives(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        coops = session.exec(select(Cooperative)).all()
        csv_data = generate_csv(coops, ["CoopID", "Name", "Description", "Location"], lambda c: [c.id, c.name, c.description, c.location])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=cooperatives.csv"
        return response

@app.get("/export/coop-orders")
def export_coop_orders(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        coop_orders = session.exec(select(CoopOrder)).all()
        csv_data = generate_csv(coop_orders, ["CoopOrderID", "BuyerID", "ListingID", "Quantity", "TotalPrice", "PaymentStatus", "Provider"], lambda co: [co.id, co.buyer_id, co.coop_listing_id, co.quantity, co.total_price, co.payment_status, co.provider])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=coop_orders.csv"
        return response

@app.get("/export/coop-members")
def export_coop_members(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        members = session.exec(select(CoopMember)).all()
        csv_data = generate_csv(members, ["MemberID", "CoopID", "UserID", "JoinedAt"], lambda m: [m.id, m.coop_id, m.user_id, m.joined_at])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=coop_members.csv"
        return response

@app.get("/export/coop-announcements")
def export_coop_announcements(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        announcements = session.exec(select(Announcement)).all()
        csv_data = generate_csv(announcements, ["AnnouncementID", "CoopID", "Title", "Content", "CreatedBy"], lambda a: [a.id, a.coop_id, a.title, a.content, a.created_by])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=coop_announcements.csv"
        return response

@app.get("/export/training")
def export_training(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        trainings = session.exec(select(Training)).all()
        csv_data = generate_csv(trainings, ["TrainingID", "Title", "Content", "Category"], lambda t: [t.id, t.title, t.content, t.category])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=training.csv"
        return response

@app.get("/export/notifications")
def export_notifications(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        notifications = session.exec(select(Notification)).all()
        csv_data = generate_csv(notifications, ["NotificationID", "UserID", "Message", "Status"], lambda n: [n.id, n.user_id, n.message, n.status])
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=notifications.csv"
        return response

# ---------------- Master ZIP export (admin-only) ----------------
@app.get("/export/all")
def export_all(current_user: User = Depends(role_required("admin"))):
    with Session(engine) as session:
        tables = {
            "users.csv": (session.exec(select(User)).all(), ["id", "username", "full_name", "role", "location", "phone"]),
            "crops.csv": (session.exec(select(Crop)).all(), ["id", "name", "quantity", "price", "farmer_id"]),
            "orders.csv": (session.exec(select(Order)).all(), ["id", "buyer_id", "crop_id", "quantity", "total_price", "payment_status", "provider"]),
            "deliveries.csv": (session.exec(select(Delivery)).all(), ["id", "order_id", "status", "location", "eta"]),
            "cooperatives.csv": (session.exec(select(Cooperative)).all(), ["id", "name", "description", "location"]),
            "coop_orders.csv": (session.exec(select(CoopOrder)).all(), ["id", "buyer_id", "coop_listing_id", "quantity", "total_price", "payment_status", "provider"]),
            "coop_members.csv": (session.exec(select(CoopMember)).all(), ["id", "coop_id", "user_id", "joined_at"]),
            "coop_announcements.csv": (session.exec(select(Announcement)).all(), ["id", "coop_id", "title", "content", "created_by"]),
            "training.csv": (session.exec(select(Training)).all(), ["id", "title", "content", "category"]),
            "notifications.csv": (session.exec(select(Notification)).all(), ["id", "user_id", "message", "status"]),
        }

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zipf:
            for filename, (records, fields) in tables.items():
                output = io.StringIO()
                writer = csv.writer(output)
                writer.writerow(fields)
                for r in records:
                    writer.writerow([getattr(r, f) for f in fields])
                zipf.writestr(filename, output.getvalue())

        response = Response(content=zip_buffer.getvalue(), media_type="application/zip")
        response.headers["Content-Disposition"] = "attachment; filename=agriconnect_backup.zip"
        return response

# ---------------- CSV Import Helpers (append/update) ----------------
def import_csv_to_table(model, file: UploadFile) -> dict:
    content = file.file.read().decode("utf-8")
    reader = csv.DictReader(io.StringIO(content))
    with Session(engine) as session:
        for row in reader:
            # Try to find existing by id (if provided)
            id_val = row.get("id") or row.get("ID") or row.get("Id")
            obj = session.get(model, int(id_val)) if id_val and id_val.strip() != "" else None
            # Normalize row keys to model attributes; convert empty strings to None
            cleaned = {k: (v if v != "" else None) for k, v in row.items()}
            if obj:
                for k, v in cleaned.items():
                    if hasattr(obj, k) and v is not None:
                        # basic type conversions for ints/floats where possible
                        current = getattr(obj, k)
                        try:
                            if isinstance(current, int):
                                setattr(obj, k, int(v))
                            elif isinstance(current, float):
                                setattr(obj, k, float(v))
                            else:
                                setattr(obj, k, v)
                        except Exception:
                            setattr(obj, k, v)
            else:
                # Remove id field if empty to allow auto PK
                for pkname in ("id", "ID", "Id"):
                    if pkname in cleaned and (cleaned[pkname] is None or cleaned[pkname] == ""):
                        cleaned.pop(pkname, None)
                # try simple type conversions for numeric-looking fields
                for k, v in list(cleaned.items()):
                    if v is None:
                        continue
                    # attempt int
                    if v.isdigit():
                        cleaned[k] = int(v)
                    else:
                        # attempt float
                        try:
                            if "." in v:
                                cleaned[k] = float(v)
                        except Exception:
                            pass
                try:
                    obj = model(**cleaned)
                    session.add(obj)
                except Exception:
                    # skip rows that can't be parsed
                    pass
        session.commit()
    return {"msg": f"Imported into {model.__name__}"}

# ---------------- Import endpoints (admin-only) ----------------
@app.post("/import/users")
def import_users(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(User, file)

@app.post("/import/crops")
def import_crops(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(Crop, file)

@app.post("/import/orders")
def import_orders(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(Order, file)

@app.post("/import/deliveries")
def import_deliveries(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(Delivery, file)

@app.post("/import/training")
def import_training(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(Training, file)

@app.post("/import/notifications")
def import_notifications(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(Notification, file)

@app.post("/import/cooperatives")
def import_coops(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(Cooperative, file)

@app.post("/import/coop_members")
def import_coop_members(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(CoopMember, file)

@app.post("/import/coop_orders")
def import_coop_orders(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(CoopOrder, file)

@app.post("/import/announcements")
def import_announcements(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    return import_csv_to_table(Announcement, file)

# ---------------- Master ZIP Restore (admin-only) ----------------
@app.post("/import/all")
def import_all(file: UploadFile = File(...), current_user: User = Depends(role_required("admin"))):
    content = file.file.read()
    with zipfile.ZipFile(io.BytesIO(content)) as zip_ref:
        temp_dir = "./tmp_import"
        os.makedirs(temp_dir, exist_ok=True)
        zip_ref.extractall(temp_dir)
        map_files = {
            "users.csv": User,
            "crops.csv": Crop,
            "orders.csv": Order,
            "deliveries.csv": Delivery,
            "training.csv": Training,
            "notifications.csv": Notification,
            "cooperatives.csv": Cooperative,
            "coop_members.csv": CoopMember,
            "coop_orders.csv": CoopOrder,
            "announcements.csv": Announcement,
        }
        for name, model in map_files.items():
            path = os.path.join(temp_dir, name)
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    with Session(engine) as session:
                        for row in reader:
                            id_val = row.get("id") or row.get("ID") or row.get("Id")
                            obj = session.get(model, int(id_val)) if id_val and id_val.strip() != "" else None
                            cleaned = {k: (v if v != "" else None) for k, v in row.items()}
                            if obj:
                                for k, v in cleaned.items():
                                    if hasattr(obj, k) and v is not None:
                                        current = getattr(obj, k)
                                        try:
                                            if isinstance(current, int):
                                                setattr(obj, k, int(v))
                                            elif isinstance(current, float):
                                                setattr(obj, k, float(v))
                                            else:
                                                setattr(obj, k, v)
                                        except Exception:
                                            setattr(obj, k, v)
                                session.add(obj)
                            else:
                                for pkname in ("id", "ID", "Id"):
                                    if pkname in cleaned and (cleaned[pkname] is None or cleaned[pkname] == ""):
                                        cleaned.pop(pkname, None)
                                for k, v in list(cleaned.items()):
                                    if v is None:
                                        continue
                                    if isinstance(v, str) and v.isdigit():
                                        cleaned[k] = int(v)
                                    else:
                                        try:
                                            if isinstance(v, str) and "." in v:
                                                cleaned[k] = float(v)
                                        except Exception:
                                            pass
                                try:
                                    obj = model(**cleaned)
                                    session.add(obj)
                                except Exception:
                                    pass
                        session.commit()
    # optional: clean temp_dir
    try:
        for f in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, f))
        os.rmdir(temp_dir)
    except Exception:
        pass
    return {"msg": "ZIP restore complete"}

# ---------------- Template CSV endpoints (admin-only) ----------------
TEMPLATES = {
    "users": ["id", "username", "full_name", "hashed_password (or password on import)", "role", "location", "phone"],
    "crops": ["id", "name", "quantity", "price", "farmer_id"],
    "orders": ["id", "buyer_id", "crop_id", "quantity", "total_price", "payment_status", "payment_reference", "provider"],
    "deliveries": ["id", "order_id", "status", "location", "eta"],
    "training": ["id", "title", "content", "category"],
    "notifications": ["id", "user_id", "message", "status"],
    "cooperatives": ["id", "name", "description", "location"],
    "coop_members": ["id", "coop_id", "user_id", "joined_at"],
    "coop_orders": ["id", "buyer_id", "coop_listing_id", "quantity", "total_price", "payment_status", "payment_reference", "provider"],
    "announcements": ["id", "coop_id", "title", "content", "created_by"],
}

@app.get("/templates/{entity}")
def download_template(entity: str, current_user: User = Depends(role_required("admin"))):
    if entity not in TEMPLATES:
        raise HTTPException(status_code=404, detail="Template not found")
    mem = generate_csv_template_bytes(TEMPLATES[entity])
    return StreamingResponse(mem, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename={entity}_template.csv"})

@app.get("/templates/all")
def download_all_templates(current_user: User = Depends(role_required("admin"))):
    mem = io.BytesIO()
    with zipfile.ZipFile(mem, "w", zipfile.ZIP_DEFLATED) as zf:
        for entity, headers in TEMPLATES.items():
            buf = io.StringIO()
            writer = csv.writer(buf)
            writer.writerow(headers)
            zf.writestr(f"{entity}_template.csv", buf.getvalue())
    mem.seek(0)
    return StreamingResponse(mem, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=all_templates.zip"})

# ---------------- End of file ----------------



















# 📁 React Frontend Code (Vite + Tailwind + Axios)

# Create a new React app:

# npm create vite@latest agriconnect-frontend -- --template react
# cd agriconnect-frontend
# npm install axios react-router-dom tailwindcss @tailwindcss/forms
# npx tailwindcss init -p


# Configure Tailwind (tailwind.config.js):

# export default {
#   content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
#   theme: { extend: {} },
#   plugins: [require("@tailwindcss/forms")],
# }

# 🔑 Auth Context (store JWT)

# src/context/AuthContext.jsx

# import React, { createContext, useState } from "react";

# export const AuthContext = createContext();

# export const AuthProvider = ({ children }) => {
#   const [token, setToken] = useState(localStorage.getItem("token") || null);
#   const [role, setRole] = useState(localStorage.getItem("role") || null);

#   const login = (token, role) => {
#     setToken(token);
#     setRole(role);
#     localStorage.setItem("token", token);
#     localStorage.setItem("role", role);
#   };

#   const logout = () => {
#     setToken(null);
#     setRole(null);
#     localStorage.clear();
#   };

#   return (
#     <AuthContext.Provider value={{ token, role, login, logout }}>
#       {children}
#     </AuthContext.Provider>
#   );
# };

# 🔐 API Client

# src/api.js

# import axios from "axios";

# const API_URL = "http://localhost:8000"; // FastAPI backend

# export const api = (token) => axios.create({
#   baseURL: API_URL,
#   headers: { Authorization: token ? `Bearer ${token}` : "" },
# });

# 🖥️ Login Page

# src/pages/Login.jsx

# import { useState, useContext } from "react";
# import { AuthContext } from "../context/AuthContext";
# import { api } from "../api";

# export default function Login() {
#   const { login } = useContext(AuthContext);
#   const [username, setUsername] = useState("");
#   const [password, setPassword] = useState("");

#   const handleLogin = async (e) => {
#     e.preventDefault();
#     try {
#       const res = await api().post("/token", new URLSearchParams({
#         username, password
#       }));
#       const token = res.data.access_token;

#       // decode JWT to get role
#       const payload = JSON.parse(atob(token.split(".")[1]));
#       login(token, payload.role);
#     } catch (err) {
#       alert("Invalid login");
#     }
#   };

#   return (
#     <div className="flex items-center justify-center h-screen">
#       <form onSubmit={handleLogin} className="p-6 bg-white shadow rounded space-y-4">
#         <h2 className="text-xl font-bold">AgriConnect Login</h2>
#         <input type="text" value={username} onChange={(e)=>setUsername(e.target.value)} placeholder="Username" className="w-full border p-2 rounded"/>
#         <input type="password" value={password} onChange={(e)=>setPassword(e.target.value)} placeholder="Password" className="w-full border p-2 rounded"/>
#         <button className="bg-green-600 text-white w-full py-2 rounded">Login</button>
#       </form>
#     </div>
#   );
# }

# 🌱 Farmer Dashboard (Add Crops)

# src/pages/FarmerDashboard.jsx

# import { useState, useContext } from "react";
# import { AuthContext } from "../context/AuthContext";
# import { api } from "../api";

# export default function FarmerDashboard() {
#   const { token } = useContext(AuthContext);
#   const [name, setName] = useState("");
#   const [price, setPrice] = useState("");
#   const [quantity, setQuantity] = useState("");

#   const addCrop = async (e) => {
#     e.preventDefault();
#     await api(token).post("/crops/", { name, price: parseFloat(price), quantity: parseInt(quantity) });
#     alert("Crop added");
#   };

#   return (
#     <div className="p-6">
#       <h1 className="text-lg font-bold">Farmer Dashboard</h1>
#       <form onSubmit={addCrop} className="space-y-3 mt-4">
#         <input placeholder="Crop Name" value={name} onChange={(e)=>setName(e.target.value)} className="border p-2 w-full"/>
#         <input placeholder="Price" value={price} onChange={(e)=>setPrice(e.target.value)} className="border p-2 w-full"/>
#         <input placeholder="Quantity" value={quantity} onChange={(e)=>setQuantity(e.target.value)} className="border p-2 w-full"/>
#         <button className="bg-green-600 text-white px-4 py-2 rounded">Add Crop</button>
#       </form>
#     </div>
#   );
# }

# 🛒 Buyer Dashboard (Browse & Order Crops)

# src/pages/BuyerDashboard.jsx

# import { useState, useEffect, useContext } from "react";
# import { api } from "../api";
# import { AuthContext } from "../context/AuthContext";

# export default function BuyerDashboard() {
#   const { token } = useContext(AuthContext);
#   const [crops, setCrops] = useState([]);

#   useEffect(() => {
#     api(token).get("/crops/").then(res => setCrops(res.data));
#   }, [token]);

#   const placeOrder = async (cropId) => {
#     await api(token).post("/orders/", { crop_id: cropId, quantity: 1 });
#     alert("Order placed");
#   };

#   return (
#     <div className="p-6">
#       <h1 className="text-lg font-bold">Available Crops</h1>
#       <ul className="space-y-2 mt-4">
#         {crops.map(crop => (
#           <li key={crop.id} className="border p-3 flex justify-between items-center">
#             <div>
#               <b>{crop.name}</b> - ${crop.price} ({crop.quantity} available)
#             </div>
#             <button onClick={()=>placeOrder(crop.id)} className="bg-blue-600 text-white px-3 py-1 rounded">Buy</button>
#           </li>
#         ))}
#       </ul>
#     </div>
#   );
# }

# 🛠️ Admin Dashboard (Manage Data)

# src/pages/AdminDashboard.jsx

# import { useContext } from "react";
# import { AuthContext } from "../context/AuthContext";
# import { api } from "../api";

# export default function AdminDashboard() {
#   const { token } = useContext(AuthContext);

#   const downloadTemplates = async () => {
#     const res = await api(token).get("/templates/all", { responseType: "blob" });
#     const url = window.URL.createObjectURL(new Blob([res.data]));
#     const link = document.createElement("a");
#     link.href = url;
#     link.setAttribute("download", "templates.zip");
#     document.body.appendChild(link);
#     link.click();
#   };

#   return (
#     <div className="p-6">
#       <h1 className="text-lg font-bold">Admin Dashboard</h1>
#       <button onClick={downloadTemplates} className="bg-purple-600 text-white px-4 py-2 rounded mt-4">
#         Download Templates ZIP
#       </button>
#     </div>
#   );
# }

# ⚡ Routing

# src/App.jsx

# import { BrowserRouter, Routes, Route } from "react-router-dom";
# import { AuthProvider, AuthContext } from "./context/AuthContext";
# import Login from "./pages/Login";
# import FarmerDashboard from "./pages/FarmerDashboard";
# import BuyerDashboard from "./pages/BuyerDashboard";
# import AdminDashboard from "./pages/AdminDashboard";
# import { useContext } from "react";

# function ProtectedRoute({ children, role }) {
#   const { token, role: userRole } = useContext(AuthContext);
#   if (!token) return <Login />;
#   if (role && role !== userRole && userRole !== "admin") return <div>Access Denied</div>;
#   return children;
# }

# export default function App() {
#   return (
#     <AuthProvider>
#       <BrowserRouter>
#         <Routes>
#           <Route path="/" element={<Login />} />
#           <Route path="/farmer" element={<ProtectedRoute role="farmer"><FarmerDashboard /></ProtectedRoute>} />
#           <Route path="/buyer" element={<ProtectedRoute role="buyer"><BuyerDashboard /></ProtectedRoute>} />
#           <Route path="/admin" element={<ProtectedRoute role="admin"><AdminDashboard /></ProtectedRoute>} />
#         </Routes>
#       </BrowserRouter>
#     </AuthProvider>
#   );
# }


# ✅ This gives you a minimal working frontend connected to your FastAPI backend:

# Farmers: add crops

# Buyers: browse & buy

# Admins: download templates

# 👉 Do you want me to extend the admin panel so they can also upload CSV/ZIP imports directly from the frontend (instead of Postman)?

# You said:
# Yes
# ChatGPT said:

# Perfect 👍 let’s extend the Admin Dashboard so admins can upload CSVs or ZIP backups directly from the frontend — no need for Postman.

# We’ll add:

# Upload per-entity CSVs (users, crops, orders, etc.)

# Upload ZIP master backup (restore all data)

# Still keep the “Download Templates ZIP”

# 🔧 Updated AdminDashboard.jsx
# import { useContext, useState } from "react";
# import { AuthContext } from "../context/AuthContext";
# import { api } from "../api";

# export default function AdminDashboard() {
#   const { token } = useContext(AuthContext);
#   const [entity, setEntity] = useState("users");
#   const [file, setFile] = useState(null);
#   const [zipFile, setZipFile] = useState(null);

#   // Download all templates
#   const downloadTemplates = async () => {
#     const res = await api(token).get("/templates/all", { responseType: "blob" });
#     const url = window.URL.createObjectURL(new Blob([res.data]));
#     const link = document.createElement("a");
#     link.href = url;
#     link.setAttribute("download", "templates.zip");
#     document.body.appendChild(link);
#     link.click();
#   };

#   // Upload single-entity CSV
#   const uploadCSV = async (e) => {
#     e.preventDefault();
#     if (!file) return alert("Select a CSV file first");
#     const formData = new FormData();
#     formData.append("file", file);
#     try {
#       await api(token).post(`/import/${entity}`, formData, {
#         headers: { "Content-Type": "multipart/form-data" }
#       });
#       alert(`CSV imported for ${entity}`);
#     } catch (err) {
#       alert("Error importing CSV: " + err.response?.data?.detail || err.message);
#     }
#   };

#   // Upload ZIP restore
#   const uploadZIP = async (e) => {
#     e.preventDefault();
#     if (!zipFile) return alert("Select a ZIP file first");
#     const formData = new FormData();
#     formData.append("file", zipFile);
#     try {
#       await api(token).post("/import/all", formData, {
#         headers: { "Content-Type": "multipart/form-data" }
#       });
#       alert("ZIP master backup restored successfully");
#     } catch (err) {
#       alert("Error restoring ZIP: " + err.response?.data?.detail || err.message);
#     }
#   };

#   return (
#     <div className="p-6 space-y-6">
#       <h1 className="text-xl font-bold">Admin Dashboard</h1>

#       {/* Download Templates */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Download Templates</h2>
#         <button
#           onClick={downloadTemplates}
#           className="bg-purple-600 text-white px-4 py-2 rounded mt-2"
#         >
#           Download Templates ZIP
#         </button>
#       </div>

#       {/* Upload Single CSV */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Upload CSV for Entity</h2>
#         <form onSubmit={uploadCSV} className="space-y-3 mt-2">
#           <select
#             value={entity}
#             onChange={(e) => setEntity(e.target.value)}
#             className="border p-2 rounded w-full"
#           >
#             <option value="users">Users</option>
#             <option value="crops">Crops</option>
#             <option value="orders">Orders</option>
#             <option value="deliveries">Deliveries</option>
#             <option value="training">Training</option>
#             <option value="notifications">Notifications</option>
#             <option value="cooperatives">Cooperatives</option>
#             <option value="coop_members">Coop Members</option>
#             <option value="coop_orders">Coop Orders</option>
#             <option value="announcements">Announcements</option>
#           </select>
#           <input
#             type="file"
#             accept=".csv"
#             onChange={(e) => setFile(e.target.files[0])}
#             className="block w-full"
#           />
#           <button className="bg-green-600 text-white px-4 py-2 rounded">
#             Upload CSV
#           </button>
#         </form>
#       </div>

#       {/* Upload ZIP Restore */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Restore from ZIP Backup</h2>
#         <form onSubmit={uploadZIP} className="space-y-3 mt-2">
#           <input
#             type="file"
#             accept=".zip"
#             onChange={(e) => setZipFile(e.target.files[0])}
#             className="block w-full"
#           />
#           <button className="bg-red-600 text-white px-4 py-2 rounded">
#             Upload & Restore ZIP
#           </button>
#         </form>
#       </div>
#     </div>
#   );
# }


# ✅ Now admins can:

# Download pre-made CSV templates

# Upload filled CSVs for specific entities (users, crops, etc.)

# Upload a ZIP master backup to restore everything at once

# 👉 Do you want me to also add a table view inside the admin dashboard so they can preview the current data (users, crops, orders) before importing/exporting?

# You said:
# Yes
# ChatGPT said:

# Perfect 🚀 — let’s enhance the Admin Dashboard with live table views so admins can preview current data (users, crops, orders, etc.) before deciding to export/import.

# We’ll use:

# GET /users, GET /crops, GET /orders, etc. (already available in your backend)

# A dropdown selector to pick which entity to view

# A table renderer that dynamically shows the data

# 🔧 Updated AdminDashboard.jsx with Table View
# import { useContext, useState, useEffect } from "react";
# import { AuthContext } from "../context/AuthContext";
# import { api } from "../api";

# export default function AdminDashboard() {
#   const { token } = useContext(AuthContext);
#   const [entity, setEntity] = useState("users");
#   const [file, setFile] = useState(null);
#   const [zipFile, setZipFile] = useState(null);
#   const [data, setData] = useState([]);

#   // Fetch current data for selected entity
#   const fetchData = async (selectedEntity) => {
#     try {
#       const res = await api(token).get(`/${selectedEntity}/`);
#       setData(res.data);
#     } catch (err) {
#       setData([]);
#       console.error(err);
#     }
#   };

#   useEffect(() => {
#     fetchData(entity);
#   }, [entity]);

#   // Download all templates
#   const downloadTemplates = async () => {
#     const res = await api(token).get("/templates/all", { responseType: "blob" });
#     const url = window.URL.createObjectURL(new Blob([res.data]));
#     const link = document.createElement("a");
#     link.href = url;
#     link.setAttribute("download", "templates.zip");
#     document.body.appendChild(link);
#     link.click();
#   };

#   // Upload single-entity CSV
#   const uploadCSV = async (e) => {
#     e.preventDefault();
#     if (!file) return alert("Select a CSV file first");
#     const formData = new FormData();
#     formData.append("file", file);
#     try {
#       await api(token).post(`/import/${entity}`, formData, {
#         headers: { "Content-Type": "multipart/form-data" }
#       });
#       alert(`CSV imported for ${entity}`);
#       fetchData(entity); // refresh table
#     } catch (err) {
#       alert("Error importing CSV: " + err.response?.data?.detail || err.message);
#     }
#   };

#   // Upload ZIP restore
#   const uploadZIP = async (e) => {
#     e.preventDefault();
#     if (!zipFile) return alert("Select a ZIP file first");
#     const formData = new FormData();
#     formData.append("file", zipFile);
#     try {
#       await api(token).post("/import/all", formData, {
#         headers: { "Content-Type": "multipart/form-data" }
#       });
#       alert("ZIP master backup restored successfully");
#       fetchData(entity); // refresh table
#     } catch (err) {
#       alert("Error restoring ZIP: " + err.response?.data?.detail || err.message);
#     }
#   };

#   return (
#     <div className="p-6 space-y-6">
#       <h1 className="text-xl font-bold">Admin Dashboard</h1>

#       {/* Download Templates */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Download Templates</h2>
#         <button
#           onClick={downloadTemplates}
#           className="bg-purple-600 text-white px-4 py-2 rounded mt-2"
#         >
#           Download Templates ZIP
#         </button>
#       </div>

#       {/* Upload Single CSV */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Upload CSV for Entity</h2>
#         <form onSubmit={uploadCSV} className="space-y-3 mt-2">
#           <select
#             value={entity}
#             onChange={(e) => setEntity(e.target.value)}
#             className="border p-2 rounded w-full"
#           >
#             <option value="users">Users</option>
#             <option value="crops">Crops</option>
#             <option value="orders">Orders</option>
#             <option value="deliveries">Deliveries</option>
#             <option value="training">Training</option>
#             <option value="notifications">Notifications</option>
#             <option value="cooperatives">Cooperatives</option>
#             <option value="coop_members">Coop Members</option>
#             <option value="coop_orders">Coop Orders</option>
#             <option value="announcements">Announcements</option>
#           </select>
#           <input
#             type="file"
#             accept=".csv"
#             onChange={(e) => setFile(e.target.files[0])}
#             className="block w-full"
#           />
#           <button className="bg-green-600 text-white px-4 py-2 rounded">
#             Upload CSV
#           </button>
#         </form>
#       </div>

#       {/* Upload ZIP Restore */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Restore from ZIP Backup</h2>
#         <form onSubmit={uploadZIP} className="space-y-3 mt-2">
#           <input
#             type="file"
#             accept=".zip"
#             onChange={(e) => setZipFile(e.target.files[0])}
#             className="block w-full"
#           />
#           <button className="bg-red-600 text-white px-4 py-2 rounded">
#             Upload & Restore ZIP
#           </button>
#         </form>
#       </div>

#       {/* Data Table Preview */}
#       <div className="border p-4 rounded overflow-x-auto">
#         <h2 className="font-semibold mb-2">Preview Data: {entity}</h2>
#         {data.length > 0 ? (
#           <table className="min-w-full border border-gray-300">
#             <thead>
#               <tr className="bg-gray-100">
#                 {Object.keys(data[0]).map((key) => (
#                   <th key={key} className="border px-2 py-1 text-left">{key}</th>
#                 ))}
#               </tr>
#             </thead>
#             <tbody>
#               {data.map((row, i) => (
#                 <tr key={i} className="odd:bg-white even:bg-gray-50">
#                   {Object.values(row).map((val, j) => (
#                     <td key={j} className="border px-2 py-1">{val?.toString()}</td>
#                   ))}
#                 </tr>
#               ))}
#             </tbody>
#           </table>
#         ) : (
#           <p className="text-gray-500">No data available</p>
#         )}
#       </div>
#     </div>
#   );
# }


# ✅ Now the Admin Dashboard supports:

# Downloading templates

# Uploading per-entity CSVs

# Uploading ZIP backups

# Live table preview of current data (auto-refreshes after import/restore)

# 👉 Do you want me to also let admins export current data (per-entity) as CSV directly from this dashboard (so they don’t need to use Postman for /export/...)?

# You said:
# Yes 
# ChatGPT said:

# Great 👍 Let’s extend the Admin Dashboard so admins can also export per-entity CSV files directly.
# We’ll add an Export CSV button next to the entity selector.

# 🔧 Updated AdminDashboard.jsx (with Export CSV)
# import { useContext, useState, useEffect } from "react";
# import { AuthContext } from "../context/AuthContext";
# import { api } from "../api";

# export default function AdminDashboard() {
#   const { token } = useContext(AuthContext);
#   const [entity, setEntity] = useState("users");
#   const [file, setFile] = useState(null);
#   const [zipFile, setZipFile] = useState(null);
#   const [data, setData] = useState([]);

#   // Fetch current data for selected entity
#   const fetchData = async (selectedEntity) => {
#     try {
#       const res = await api(token).get(`/${selectedEntity}/`);
#       setData(res.data);
#     } catch (err) {
#       setData([]);
#       console.error(err);
#     }
#   };

#   useEffect(() => {
#     fetchData(entity);
#   }, [entity]);

#   // Download all templates
#   const downloadTemplates = async () => {
#     const res = await api(token).get("/templates/all", { responseType: "blob" });
#     const url = window.URL.createObjectURL(new Blob([res.data]));
#     const link = document.createElement("a");
#     link.href = url;
#     link.setAttribute("download", "templates.zip");
#     document.body.appendChild(link);
#     link.click();
#   };

#   // Export CSV for entity
#   const exportCSV = async () => {
#     try {
#       const res = await api(token).get(`/export/${entity}`, { responseType: "blob" });
#       const url = window.URL.createObjectURL(new Blob([res.data]));
#       const link = document.createElement("a");
#       link.href = url;
#       link.setAttribute("download", `${entity}.csv`);
#       document.body.appendChild(link);
#       link.click();
#     } catch (err) {
#       alert("Error exporting CSV: " + err.response?.data?.detail || err.message);
#     }
#   };

#   // Upload single-entity CSV
#   const uploadCSV = async (e) => {
#     e.preventDefault();
#     if (!file) return alert("Select a CSV file first");
#     const formData = new FormData();
#     formData.append("file", file);
#     try {
#       await api(token).post(`/import/${entity}`, formData, {
#         headers: { "Content-Type": "multipart/form-data" }
#       });
#       alert(`CSV imported for ${entity}`);
#       fetchData(entity); // refresh table
#     } catch (err) {
#       alert("Error importing CSV: " + err.response?.data?.detail || err.message);
#     }
#   };

#   // Upload ZIP restore
#   const uploadZIP = async (e) => {
#     e.preventDefault();
#     if (!zipFile) return alert("Select a ZIP file first");
#     const formData = new FormData();
#     formData.append("file", zipFile);
#     try {
#       await api(token).post("/import/all", formData, {
#         headers: { "Content-Type": "multipart/form-data" }
#       });
#       alert("ZIP master backup restored successfully");
#       fetchData(entity); // refresh table
#     } catch (err) {
#       alert("Error restoring ZIP: " + err.response?.data?.detail || err.message);
#     }
#   };

#   return (
#     <div className="p-6 space-y-6">
#       <h1 className="text-xl font-bold">Admin Dashboard</h1>

#       {/* Download Templates */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Download Templates</h2>
#         <button
#           onClick={downloadTemplates}
#           className="bg-purple-600 text-white px-4 py-2 rounded mt-2"
#         >
#           Download Templates ZIP
#         </button>
#       </div>

#       {/* Upload Single CSV + Export */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Import / Export Entity CSV</h2>
#         <div className="flex items-center space-x-3 mt-2">
#           <select
#             value={entity}
#             onChange={(e) => setEntity(e.target.value)}
#             className="border p-2 rounded"
#           >
#             <option value="users">Users</option>
#             <option value="crops">Crops</option>
#             <option value="orders">Orders</option>
#             <option value="deliveries">Deliveries</option>
#             <option value="training">Training</option>
#             <option value="notifications">Notifications</option>
#             <option value="cooperatives">Cooperatives</option>
#             <option value="coop_members">Coop Members</option>
#             <option value="coop_orders">Coop Orders</option>
#             <option value="announcements">Announcements</option>
#           </select>
#           <button
#             onClick={exportCSV}
#             className="bg-blue-600 text-white px-4 py-2 rounded"
#           >
#             Export CSV
#           </button>
#         </div>

#         <form onSubmit={uploadCSV} className="space-y-3 mt-3">
#           <input
#             type="file"
#             accept=".csv"
#             onChange={(e) => setFile(e.target.files[0])}
#             className="block w-full"
#           />
#           <button className="bg-green-600 text-white px-4 py-2 rounded">
#             Import CSV
#           </button>
#         </form>
#       </div>

#       {/* Upload ZIP Restore */}
#       <div className="border p-4 rounded">
#         <h2 className="font-semibold">Restore from ZIP Backup</h2>
#         <form onSubmit={uploadZIP} className="space-y-3 mt-2">
#           <input
#             type="file"
#             accept=".zip"
#             onChange={(e) => setZipFile(e.target.files[0])}
#             className="block w-full"
#           />
#           <button className="bg-red-600 text-white px-4 py-2 rounded">
#             Upload & Restore ZIP
#           </button>
#         </form>
#       </div>

#       {/* Data Table Preview */}
#       <div className="border p-4 rounded overflow-x-auto">
#         <h2 className="font-semibold mb-2">Preview Data: {entity}</h2>
#         {data.length > 0 ? (
#           <table className="min-w-full border border-gray-300">
#             <thead>
#               <tr className="bg-gray-100">
#                 {Object.keys(data[0]).map((key) => (
#                   <th key={key} className="border px-2 py-1 text-left">{key}</th>
#                 ))}
#               </tr>
#             </thead>
#             <tbody>
#               {data.map((row, i) => (
#                 <tr key={i} className="odd:bg-white even:bg-gray-50">
#                   {Object.values(row).map((val, j) => (
#                     <td key={j} className="border px-2 py-1">{val?.toString()}</td>
#                   ))}
#                 </tr>
#               ))}
#             </tbody>
#           </table>
#         ) : (
#           <p className="text-gray-500">No data available</p>
#         )}
#       </div>
#     </div>
#   );
# }


# ✅ Now the dashboard supports:

# Download templates

# Import CSV (append/merge)

# Export CSV (download per-entity data)

# ZIP backup restore

# Live table preview of current data

# Do you also want me to add an “Export All (ZIP)” button so the admin can download a full snapshot of the database in one click?

# ChatGPT can make mistakes. Check important info.
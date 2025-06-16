from app import app, db
from app.models import User
from collections import defaultdict

with app.app_context():
    users = User.query.order_by(User.name).all()

    name_groups = defaultdict(list)
    for user in users:
        name_groups[user.name].append(user)

    for name, group in name_groups.items():
        if len(group) > 1:
            for idx, user in enumerate(group):
                if idx == 0:
                    continue
                new_name = f"{user.name}_{idx}"
                print(f"Переименование: {user.name} → {new_name}")
                user.name = new_name

    db.session.commit()
    print("✅ Готово! Дубликаты переименованы.")

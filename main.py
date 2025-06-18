import json

f = open('contacts.json', 'w')
f.write('{"contacts": []}')
f.close()


def show_menu() -> None:
    """Konsolda foydalanuvchi uchun menyuni chiqaradi."""
    print("\n====== 📱 Contact Book ======")
    print("1. ➕ Yangi kontakt qo‘shish")
    print("2. 📄 Barcha kontaktlarni ko‘rish")
    print("3. 🔍 Kontaktni ism bo‘yicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni ko‘rish")
    print("5. 🚪 Dasturni yakunlash")


def add_contact() -> None:
    """
    Yangi kontakt qo‘shadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    print("Yangi contact malumotlarini kiriting")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    f = open('contacts.json')
    contacts = json.loads(f.read())
    f.close()

    contacts["contacts"].append(contact)

    f = open('contacts.json', 'w')
    contacts_json = json.dumps(contacts, indent=4)
    f.write(contacts_json)
    f.close()


def list_contacts() -> None:
    """
    Kontaktlar ro‘yxatini konsolga chiqaradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    pass


def search_contact() -> None:
    """
    Foydalanuvchi kiritgan ism bo‘yicha kontaktlarni qidiradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    pass


def filter_gmail_contacts() -> None:
    """
    Faqat @gmail.com domeniga ega kontaktlarni ko‘rsatadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    pass


def main() -> None:
    """
    Dasturning asosiy ishga tushirish funksiyasi.
    Menyu orqali foydalanuvchi tanlovini boshqaradi.
    """

    while True:
        show_menu()
        choice = input("Tanlov (1–5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            filter_gmail_contacts()
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("❗️Noto‘g‘ri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")


main()
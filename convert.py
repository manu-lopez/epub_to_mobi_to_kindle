import os, time
from dotenv import load_dotenv
load_dotenv()


def epub_to_mobi(from_path):
    to_path = os.getenv("to_path")

    # Recorro todos los archivos de la ruta, realizo conversion y envio a email de kindle
    for root, dirs, files in os.walk(from_path):
        for onefile in files:
            original_ebook = os.path.join(root, onefile)
            name, ext = os.path.splitext(onefile)

            if ext == ".epub":
                try:
                    os.system("ebook-convert '"+ original_ebook + "' '" + os.path.join(to_path, name + '.mobi') +"'")
                except:
                    print("Error during conversion")
                
                try:
                    send_email(os.path.join(to_path, name + '.mobi'))
                    time.sleep(10)
                    os.remove(original_ebook)
                    print("Removing files...")
                except:
                    print("Error sending email")


def send_email(file_to_send):
    user=os.getenv("user")
    password=os.getenv("password")
    user_mail=os.getenv("user_mail")
    kindle_mail=os.getenv("kindle_mail")

    os.system("calibre-smtp -a '"+ file_to_send +"' -r smtp.gmail.com --port 587 -u " + user + " -p " + password + " " + user_mail + " " + kindle_mail + " Ebook")
    print("Ebook sent...")

epub_to_mobi(os.getenv("from_path"))
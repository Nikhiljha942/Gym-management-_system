import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class GymManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NIKHIL FITNESS CLUB")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        # Title
        title_label = tk.Label(self.root, text="Welcome to NIKHIL FITNESS CLUB", 
                               font=("Helvetica", 18, "bold"), bg="#000000", fg="#ff0000")
        title_label.pack(pady=20)

        # Member Management Frame
        member_frame = ttk.LabelFrame(self.root, text="Member Management", padding=(20, 10))
        member_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Entry Fields
        self.member_id_entry = ttk.Entry(member_frame, width=20)
        self.member_id_entry.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="Member ID:").grid(row=0, column=0, padx=10, pady=10)

        self.first_name_entry = ttk.Entry(member_frame, width=20)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="First Name:").grid(row=1, column=0, padx=10, pady=10)

        self.last_name_entry = ttk.Entry(member_frame, width=20)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="Last Name:").grid(row=2, column=0, padx=10, pady=10)

        self.dob_entry = ttk.Entry(member_frame, width=20)
        self.dob_entry.grid(row=3, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="Date of Birth (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=10)

        self.join_date_entry = ttk.Entry(member_frame, width=20)
        self.join_date_entry.grid(row=4, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="Join Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=10)

        self.membership_id_entry = ttk.Entry(member_frame, width=20)
        self.membership_id_entry.grid(row=5, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="Membership ID:").grid(row=5, column=0, padx=10, pady=10)

        self.phone_entry = ttk.Entry(member_frame, width=20)
        self.phone_entry.grid(row=6, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="Phone Number:").grid(row=6, column=0, padx=10, pady=10)

        self.email_entry = ttk.Entry(member_frame, width=20)
        self.email_entry.grid(row=7, column=1, padx=10, pady=10)
        ttk.Label(member_frame, text="Email:").grid(row=7, column=0, padx=10, pady=10)

        # Buttons
        add_member_button = ttk.Button(member_frame, text="Add Member", command=self.add_member)
        add_member_button.grid(row=8, column=0, columnspan=2, pady=20)

        view_members_button = ttk.Button(member_frame, text="View Members", command=self.view_members)
        view_members_button.grid(row=9, column=0, columnspan=2)

    def add_member(self):
        member_id = self.member_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get()
        join_date = self.join_date_entry.get()
        membership_id = self.membership_id_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Insert member into the database
        try:
            # Connect to your MySQL database
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Nikhilkj@d21',
                database='GymManagement'
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Members (MemberID, FirstName, LastName, DOB, JoinDate, MembershipID, PhoneNumber, Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (member_id, first_name, last_name, dob, join_date, membership_id, phone, email))
            connection.commit()
            messagebox.showinfo("Success", "Member added successfully!")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def view_members(self):
        # Display members (implement your logic to fetch and display members)
        messagebox.showinfo("Info", "Display members functionality not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GymManagementApp(root)
    root.mainloop()

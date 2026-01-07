import customtkinter as ctk
import requests
import tkinter as tk


API_URL = "http://127.0.0.1:5000/api/creatures"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Creature Manager")
app.geometry("900x500")

selected_creature_id = None


def clear_form():
    name_entry.delete(0, "end")
    max_hp_entry.delete(0, "end")
    atm_hp_entry.delete(0, "end")
    info_entry.delete("1.0", "end")


def load_creatures():
    creature_listbox.delete(0, "end")
    try:
        response = requests.get(API_URL + "/")
        creatures = response.json()

        for c in creatures:
            display = f"{c['id']} | {c['name']} | {c['atm_hp']}/{c['max_hp']}"
            creature_listbox.insert("end", display)
    except Exception as e:
        creature_listbox.insert("end", f"Error: {e}")


def get_selected_creature_id():
    selection = creature_listbox.curselection()
    if not selection:
        return None
    text = creature_listbox.get(selection[0])
    return int(text.split("|")[0].strip())


def on_select_creature(event):
    selection = creature_listbox.curselection()
    if not selection:
        return

    text = creature_listbox.get(selection[0])
    creature_id = int(text.split("|")[0].strip())

    try:
        response = requests.get(API_URL + "/")
        creatures = response.json()
        for c in creatures:
            if c["id"] == creature_id:
                clear_form()
                name_entry.insert(0, c["name"])
                max_hp_entry.insert(0, c["max_hp"])
                atm_hp_entry.insert(0, c["atm_hp"])
                info_entry.insert("1.0", c["additional_info"] or "")
                break
    except Exception as e:
        print("Select error:", e)

def build_creature_data():
    name = name_entry.get().strip()
    max_hp_raw = max_hp_entry.get().strip()
    atm_hp_raw = atm_hp_entry.get().strip()
    info = info_entry.get("1.0", "end").strip()

    if not name or not max_hp_raw.isdigit():
        return None

    data = {
        "name": name,
        "max_hp": int(max_hp_raw),
        "atm_hp": int(atm_hp_raw) if atm_hp_raw.isdigit() else 0,
        "additional_info": info
    }

    return data


def create_creature():
    data = build_creature_data()
    if not data:
        return

    try:
        requests.post(API_URL + "/", json=data)
        load_creatures()
        clear_form()
    except Exception as e:
        print("Create error:", e)


def update_creature():
    creature_id = get_selected_creature_id()
    if not creature_id:
        return

    data = build_creature_data()
    if not data:
        return

    try:
        requests.put(f"{API_URL}/{creature_id}", json=data)
        load_creatures()
        clear_form()
    except Exception as e:
        print("Update error:", e)


def delete_creature():
    creature_id = get_selected_creature_id()
    if not creature_id:
        print("No creature selected")
        return

    try:
        requests.delete(f"{API_URL}/{creature_id}")
        load_creatures()
        clear_form()
    except Exception as e:
        print("Delete error:", e)


main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = ctk.CTkFrame(main_frame, width=300)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)


ctk.CTkLabel(left_frame, text="Name").pack(anchor="w")
name_entry = ctk.CTkEntry(left_frame)
name_entry.pack(fill="x", pady=5)

ctk.CTkLabel(left_frame, text="Max HP").pack(anchor="w")
max_hp_entry = ctk.CTkEntry(left_frame)
max_hp_entry.pack(fill="x", pady=5)

ctk.CTkLabel(left_frame, text="Current HP").pack(anchor="w")
atm_hp_entry = ctk.CTkEntry(left_frame)
atm_hp_entry.pack(fill="x", pady=5)

ctk.CTkLabel(left_frame, text="Additional Info").pack(anchor="w")
info_entry = ctk.CTkTextbox(left_frame, height=80)
info_entry.pack(fill="x", pady=5)

create_btn = ctk.CTkButton(left_frame, text="Create Creature", command=create_creature)
create_btn.pack(fill="x", pady=5)

update_btn = ctk.CTkButton(left_frame, text="Update Creature", command=update_creature)
update_btn.pack(fill="x", pady=5)

delete_btn = ctk.CTkButton(left_frame, text="Delete Creature", command=delete_creature)
delete_btn.pack(fill="x", pady=5)


ctk.CTkLabel(right_frame, text="Creatures").pack(anchor="w")

creature_listbox = tk.Listbox(
    right_frame,
    bg="#1e1e1e",
    fg="white",
    selectbackground="#3b82f6",
    activestyle="none"
)

creature_listbox.pack(fill="both", expand=True, padx=5, pady=5)
creature_listbox.bind("<<ListboxSelect>>", on_select_creature)


load_creatures()
app.mainloop()

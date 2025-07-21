import tkinter as tk
import tkinter.messagebox 
import json  

file_name = "tasks.json"  # Görevlerin depolamak için tasks adında JSON dosyası oluşturdum.

tasks = []  # Görevlerin atanacağı liste
completed_tasks = []  # Tamamlanan görevlerin atanacağı liste

# Görev ekleme fonksiyonu
def add_task():   
    task = entry.get().strip()  # Giriş kutusundan alınan görev
    if task:  # Eğer görev boş değilse devam et
        response = tkinter.messagebox.askyesno("Onay", f"{task} görevini eklemek istiyor musunuz?")  #Görevin eklenip eklenmemesi gerektiği sorusu
        if response:  # Eğer kullanıcı onaylarsa
            tasks.append(task)  # Görevi tasks listesine ekle
            listbox.insert(tk.END, task)  # Görevi penceredeki listeye ekle
            entry.delete(0, tk.END)  # Giriş kutusunu temizliyoruz
            save_tasks()  # Görevleri dosyaya kaydet
    else:  # Eğer görev boş ise uyarı ver
        tkinter.messagebox.showwarning("Uyarı", "Boş görev eklenemez!")

# Görev silme fonksiyonu
def delete_task():
    try:
        task_index = listbox.curselection()[0]  # Seçili görevin indeksini belirleme
        deleted_task = tasks[task_index]  # Silinen görevi silinenler listesine ata
        listbox.delete(task_index)  # Görevi penceredeki listeden sil
        del tasks[task_index]  # Görevi listeden sil
        save_tasks()  # Görevleri dosyaya kaydet
        tkinter.messagebox.showinfo("Bilgi", "Görev silindi: " + deleted_task)  # Silinen görev hakkında bilgi ver
    except IndexError:  # Eğer bir görev seçilmediyse uyarı ver
        tkinter.messagebox.showwarning("Uyarı", "Lütfen bir görev seçin!")

# Görevi tamamlama fonksiyonu
def mark_complete():
    try:
        task_index = listbox.curselection()[0]  # Seçili görevin indeksini kaydet
        completed_task = tasks.pop(task_index)  # Tamamlanan görevi listeden çıkar ve sakla
        listbox.delete(task_index)  # Görevi penceredeki listeden sil
        completed_tasks.append(completed_task)  # Tamamlanan görevi tamamlanan listesine ekle
        completed_listbox.insert(tk.END, completed_task)  # Tamamlanan görevi tamamlananlar listesine ekle
        save_tasks()  # Görevleri dosyaya kaydet
        tkinter.messagebox.showinfo("Bilgi", f"{completed_task} görevi tamamlandı!")  # Tamamlanan görev hakkında bilgi veriyor
    except IndexError:  # Eğer bir görev seçilmediyse devam etme
        pass

# Görevleri dosyaya kaydetme fonksiyonu
def save_tasks():
    with open(file_name, "w") as file:  # Dosyayı yazma modunda aç
        json.dump({"tasks": tasks, "completed_tasks": completed_tasks}, file)  # Görevleri JSON formatında dosyaya yaz
     
# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("To-Do List")  # Pencere başlığı
root.configure(bg="light blue")  # Pencere arka plan rengi

# Ana frame oluşturma
main_frame = tk.Frame(root, bg="light blue")  # Ana frame oluşturuldu ve rengi açık mavi olarak belirlendi
main_frame.pack(pady=10)  # Ana frame arayüzde yerleşimi

# Sol frame oluşturma (tamamlanmamış görevler listesinin bulunacağı yer)
left_frame = tk.Frame(main_frame, bg="light blue")  # Sol frame oluşturuldu rengi de açık mavi olarak belirlendi
left_frame.pack(side=tk.LEFT, padx=10)  # Sol frame'in yerleşimi

# Sağ frame oluşturma (tamamlanan görevler listesinin bulunacağı yer)
right_frame = tk.Frame(main_frame, bg="light blue")  # Sağ frame oluşturuldu rengi de açık mavi olarak belirlendi
right_frame.pack(side=tk.RIGHT, padx=10)  # Sağ frame'in yerleşimi

# Sol taraftaki görevlerin listeleneceği alan
label_left = tk.Label(left_frame, text="Tamamlanmamış Görevler", font=("Helvetica", 12, "bold"), bg="light blue")
label_left.pack()  # Etiketin arayüzde yerleşimi

scrollbar_left = tk.Scrollbar(left_frame, orient=tk.VERTICAL)  # Scrollbar oluşturuldu
scrollbar_left.pack(side=tk.RIGHT, fill=tk.Y)  # Scrollbar'ın tamamlanmamış görevler listesindeki yerleşimi

listbox = tk.Listbox(left_frame, width=30, height=10, bd=0, font=("Helvetica", 12), yscrollcommand=scrollbar_left.set)
listbox.pack()  # Listbox'ın arayüzde yerleşimi

scrollbar_left.config(command=listbox.yview)  # Scrollbar'ın listbox ile ilişkilendirilmesi

# Sağ taraftaki tamamlanan görevlerin listeleneceği alan
label_right = tk.Label(right_frame, text="Tamamlanan Görevler", font=("Helvetica", 12, "bold"), bg="light blue")
label_right.pack()  # Etiketin arayüzde yerleşimi

scrollbar_right = tk.Scrollbar(right_frame, orient=tk.VERTICAL)  # Scrollbar oluşturuldu
scrollbar_right.pack(side=tk.RIGHT, fill=tk.Y)  # Scrollbar'ın tamamlanmış görevler listesindeki yerleşimi

completed_listbox = tk.Listbox(right_frame, width=30, height=10, bd=0, font=("Helvetica", 12), yscrollcommand=scrollbar_right.set)
completed_listbox.pack()  # Listbox'ın arayüzde yerleşimi

scrollbar_right.config(command=completed_listbox.yview)  # Scrollbar'ın listbox ile ilişkilendirilmesi

# Görev eklemek için giriş alanı
entry_frame = tk.Frame(root, bg="light blue")  # Giriş alanı için frame oluşturuldu
entry_frame.pack()  # Giriş alanının arayüzde yerleşimi

entry = tk.Entry(entry_frame, font=("Helvetica", 12))  # Giriş kutusu
entry.pack(pady=10)  # Giriş kutusunun yerleşimi

# Butonlar için frame oluşturma
button_frame = tk.Frame(root, bg="light blue")  # Butonlar için frame oluşturuldu
button_frame.pack()  # Butonların arayüzde yerleşimi

# Görev ekleme, silme ve tamamlama butonları
add_button = tk.Button(button_frame, text="Görev Ekle", width=15, command=add_task)  # Görev ekleme butonu
add_button.pack(side=tk.LEFT, padx=5)  # Görev ekleme butonun arayüzde yerleşimi

delete_button = tk.Button(button_frame, text="Görev Sil", width=15, command=delete_task)  # Görev silme butonu
delete_button.pack(side=tk.LEFT, padx=5)  # Görev silme butonun arayüzde yerleşimi

complete_button = tk.Button(button_frame, text="Tamamlandı", width=15, command=mark_complete)  # Görev tamamlama butonu
complete_button.pack(side=tk.LEFT, padx=5)  # Görev tamamlama butonun arayüzde yerleşimi


# Pencereyi açma ve çalıştırma
root.mainloop()


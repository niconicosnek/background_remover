import os
from tkinter import Tk, Label, Button, filedialog, Frame
from rembg import remove
from PIL import Image, ImageTk

# Gera um nome de saída disponível na mesma pasta da imagem original
def get_available_output_path(input_path):
    base_dir = os.path.dirname(input_path)
    base_filename = os.path.join(base_dir, "output")

    if not os.path.exists(base_filename + '.png'):
        return base_filename + '.png'

    index = 2
    while True:
        candidate = f"{base_filename}{index}.png"
        if not os.path.exists(candidate):
            return candidate
        index += 1

# Processa a imagem e salva com nome adequado
def process_image(filepath):
    try:
        status_label.config(text="Processando imagem...")  # Mensagem temporária

        input_image = Image.open(filepath)
        output_image = remove(input_image)
        input_image.close()  # Garante que o arquivo de entrada seja liberado

        output_path = get_available_output_path(filepath)
        output_image.save(output_path)

        status_label.config(text=f"Imagem salva como: {output_path}")
    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}")

# Ação do botão de procurar imagem
def browse_image():
    filepath = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.webp;*.bmp")]
    )
    if filepath:
        process_image(filepath)

# Permitir arrastar e soltar arquivos
def drop(event):
    filepath = event.data.strip('{}')  # Corrige nome de arquivo com espaços
    if os.path.isfile(filepath):
        process_image(filepath)

# Interface principal
try:
    import tkinterdnd2 as tkdnd  # Instale com: pip install tkinterdnd2
except ImportError:
    raise ImportError("Você precisa instalar 'tkinterdnd2' com: pip install tkinterdnd2")

class App(tkdnd.TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Removedor de Fundo")
        self.geometry("550x250")
        self.configure(bg="#f0f0f0")

        # Botão
        Button(self, text="Procurar Imagem", command=browse_image, width=30).pack(pady=10)

        # Área de soltar imagem
        drop_frame = Frame(self, width=350, height=120, bg="#e0e0e0", relief="ridge", bd=2)
        drop_frame.pack(pady=10)
        drop_label = Label(drop_frame, text="Arraste e solte a imagem aqui", bg="#e0e0e0")
        drop_label.place(relx=0.5, rely=0.5, anchor="center")
        drop_frame.drop_target_register(tkdnd.DND_FILES)
        drop_frame.dnd_bind('<<Drop>>', drop)

        # Status
        global status_label
        status_label = Label(self, text="", fg="green", bg="#f0f0f0")
        status_label.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()

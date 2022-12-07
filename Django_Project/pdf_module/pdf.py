from fpdf import FPDF
import qrcode
import random 
import os
import hashlib
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d")

def make_pdf(titular = "placeholder", n = 0, f = 0, date_factura = now, date_entradas = now, park = "None", total = 0, data_in = 1):
  #data = str(id_factura)
  data = str(data_in)
  string = hashlib.sha256(data.encode()).hexdigest()
  img = qrcode.make(string) # qrcode.image.pil.PilImage
  img_path = f"pdf_module/{string}.png" 
  img.save(img_path)

  lor = '   Lorem, ipsum dolor sit amet consectetur adipisicing elit. Atque laudantium dicta magnam. Harum vel ex repellat ipsum nihil doloremque tempore labore voluptatum fugit dignissimos odio, mollitia assumenda hic sint cum velit recusandae omnis aliquid at neque veniam sunt alias. Quod culpa, corporis blanditiis quis minima debitis ut voluptate nam ipsum!' 


  WIDTH = 210
  HEIGHT = 297
  pdf = FPDF()
  pdf.add_page()
  pdf.image("pdf_module/bkg.jpg", 0, 0, WIDTH)
  pdf.image(img_path, WIDTH/4, HEIGHT/3, WIDTH/2)

  pdf.set_font('Courier', 'B', 25)
  pdf.cell(30, 5, 'Detalle de la compra')
  pdf.ln(10)
  pdf.set_font('Courier', 'B', 16)
  pdf.cell(5, 5, f'Titular: {titular}')
  pdf.ln(10)
  pdf.cell(5, 5, f'Cantidad Entradas: {n+f}')
  pdf.ln(10)
  pdf.cell(5, 5, f'Fast-Pass: {f} \t // \t Normal: {n} ')
  pdf.ln(10)
  pdf.cell(5, 5, f'Fecha de Compra: {date_factura}')
  pdf.ln(10)
  pdf.cell(5, 5, f'Fecha de Boletos: {date_entradas}')
  pdf.ln(10)
  pdf.cell(5, 5, f'Parque: {park}')
  pdf.ln(10)
  pdf.cell(5, 5, f'Precio: {total}')
  pdf.set_y(HEIGHT-70)
  pdf.write(5,'Información:')
  pdf.ln(5)
  pdf.write(5, lor)
  pdf.output(f'pdf_module/{string}.pdf', 'F')
  #os.remove(img_path)
  return f'pdf_module/{string}.pdf'
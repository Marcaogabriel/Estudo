import win32com.client as win32

# enviar um email automatico
outlook = win32.Dispatch('outlook.application') # -> Aplicação para enviar
mail = outlook.CreateItem(0) # -> Aplicação para enviar criada
mail.To = 'kaualucaskl2@gmail.com' # -> Para quem vai enviar
mail.Subject = 'Seu Produto saiu para a entrega!!' # -> Tema do Texto
mail.HTMLBody = ''' <p>Seu produto saiu para a entrega e chegará em até 48 horas.</p> 
<p> Tente ficar em casa. Caso não receba o produto, ele estará na agência dos Correios mais próxima. </p>
<p> Boa tarde </p>''' # -> Escrita do texto

mail.Send() # -> Enviar email

print('Email enviado!!')

# <p> -> fazer pular linha
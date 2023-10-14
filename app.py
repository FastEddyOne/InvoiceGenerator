import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_user_input():
    try:
        company_info = {
            "name": input("Enter company name: "),
            "address": input("Enter company address: "),
            "city": input("Enter company city: "),
            "state": input("Enter company state: "),
            "zipcode": input("Enter company zipcode: "),
            # ... other company details
        }

        customer_info = {
            "name": input("Enter customer name: "),
            "address": input("Enter customer address: "),
            "city": input("Enter customer city: "),
            "state": input("Enter customer state: "),
            "zipcode": input("Enter customer zipcode: "),
            # ... other customer details
        }

        items = []
        num_items = int(input_with_validation("Enter the number of items: ", int))
        for _ in range(num_items):
            description = input("Enter item description: ")
            price = input_with_validation("Enter item price: ", float)
            quantity = input_with_validation("Enter item quantity: ", int)
            items.append({"description": description, "price": price, "quantity": quantity})

        return {"company": company_info, "customer": customer_info, "items": items}

    except ValueError as e:
        print(f"Invalid input: {e}", file=sys.stderr)
        sys.exit(1)


def input_with_validation(prompt, expected_type):
    while True:
        user_input = input(prompt)
        try:
            validated_input = expected_type(user_input)
            return validated_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {expected_type.__name__}.")

def draw_text(canvas, data, x, y):
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(x, y, data.get("name", ""))
    
    canvas.setFont("Helvetica", 10)
    canvas.drawString(x, y-20, data.get("address", ""))
    canvas.drawString(x, y-35, f'{data.get("city", "")}, {data.get("state", "")} {data.get("zipcode", "")}')

def draw_invoice(canvas, invoice_data, width, height):
    # Draw Company Information
    draw_text(canvas, invoice_data["company"], 50, height-50)
    
    # Draw Customer Information
    draw_text(canvas, invoice_data["customer"], 350, height-50)
    
    # Draw Item Table Headers
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(50, height-150, "Description")
    # ... other headers
    
    # Draw Items and Calculate Total
    total_amount = draw_items(canvas, invoice_data["items"], height-170)

    # Draw Total Amount
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(400, height-170-20*(len(invoice_data["items"])+1), "Total:")
    canvas.drawString(500, height-170-20*(len(invoice_data["items"])+1), f"${total_amount:.2f}")

def draw_text(canvas, data, x, y):
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(x, y, data["name"])
    
    canvas.setFont("Helvetica", 10)
    canvas.drawString(x, y-20, data["address"])
    canvas.drawString(x, y-35, f'{data["city"]}, {data.get("state", "")} {data["zipcode"]}')
    # ... other data

def draw_items(canvas, items, start_y):
    y_pos = start_y
    total_amount = 0
    
    canvas.setFont("Helvetica", 10)
    for item in items:
        canvas.drawString(50, y_pos, item["description"])
        canvas.drawString(300, y_pos, str(item["quantity"]))
        canvas.drawString(400, y_pos, f"${item['price']:.2f}")
        canvas.drawString(500, y_pos, f"${item['price']*item['quantity']:.2f}")
        
        total_amount += item['price']*item['quantity']
        y_pos -= 20
    
    return total_amount

def create_invoice(file_path, invoice_data):
    try:
        width, height = letter
        my_canvas = canvas.Canvas(file_path, pagesize=letter)
        draw_invoice(my_canvas, invoice_data, width, height)
        my_canvas.save()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    user_input_data = get_user_input()
    create_invoice("InvoiceGenerator/invoice.pdf", user_input_data)
    print("Invoice generated successfully!")

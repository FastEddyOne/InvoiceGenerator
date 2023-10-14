# Invoice Generator

Invoice Generator is a straightforward Python script to generate simple PDF invoices. Utilizing the `reportlab` library, it allows user inputs for company and customer details, along with item particulars, to craft a structured invoice.

## Prerequisites

Ensure that you have **Python 3.x** and the `reportlab` library installed. To install `reportlab`, run:

```sh
pip install reportlab
```

## Usage

1. **Run the Script:**
   Navigate to the script directory and execute the Python script using:
   ```sh
   python app.py
   ```

2. **Enter the Details:**
   Follow the command-line prompts to input details for the company, customer, and items.

3. **Generate the Invoice:**
   Upon providing all the necessary details, the script generates a PDF invoice, saving it in the `InvoiceGenerator` directory.

## Code Structure

- **`get_user_input()`:** Gathers and returns user inputs related to company, customer, and item details.
  
- **`input_with_validation(prompt, expected_type)`:** Facilitates user input with validation to confirm the accurate data type.

- **`draw_text(canvas, data, x, y)`:** Renders text onto the PDF canvas with specified data and coordinates.

- **`draw_invoice(canvas, invoice_data, width, height)`:** Illustrates the entire invoice onto the canvas using the provided user data.

- **`draw_items(canvas, items, start_y)`:** Details item information on the canvas and computes the total amount.

- **`create_invoice(file_path, invoice_data)`:** Generates the PDF for the invoice, managing potential exceptions during file creation.

## Notes

- Ensure the directory intended for storing the PDF is present, or modify the script to manage directory creation.
  
- While data validation is performed for user inputs to ensure appropriate data types, additional validation (e.g., checking realistic prices or zip code formats) might be considered per use case.

- This script serves as a basic foundation and can be extended to accommodate additional features like various tax rates, further item details, or enhanced formatting options.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

- Gratitude towards the `reportlab` community for providing a robust library for PDF generation in Python.


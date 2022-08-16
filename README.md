# autofill-google-form

## Installation

1. `pip install -r requirements.txt`
2. `cp form.json.sample form.json`

## Usage

1. Fill out `form.json`
   - `form_url`: Form's URL which is ends with **`viewform`**.
   - `answers`: Each element corresponds to the answer to each question.
2. Run `python3 main.py`
3. Here's the supported type of answer
   - `Short Answer`: [string]
   - `Paragraph`: [string]
   - `Dropdown`: [string], option's text
   - `Multiple Choice`: [string], option's text
   - `Checkbox`: [list], option's text
   - `Date`: [string], format: yyyy-mm-dd
   - `Time` [string], format: HH:MM

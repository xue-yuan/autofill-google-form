# autofill-google-form

## 2022-04-13 Update

Google has modified the dom elements and request format, this script is no longer available.

## Installation

1. `pip install -r requirements.txt`
2. `cp autofill.json.sample autofill.json`

## Usage

1. Fill out `autofill.json`
   - `form-url`: Form's URL which is ends with **`viewform`**.
   - `response`: Each element corresponds to the response to each question
2. Here's the supported type of question
   - `Short Answer`: [string]
   - `Paragraph`: [string]
   - `Dropdown`: [string], option's text
   - `Multiple Choice`: [string], option's text
   - `Checkbox`: [list], option's text
   - `Date`: [string], format: yyyy-mm-dd
   - `Time` [string], format: HH:MM

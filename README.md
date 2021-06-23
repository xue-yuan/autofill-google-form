# autofill-google-form

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

# Your Life in Numbers

Python Essentials Project Portfolio - Code Institute

View the deployed site [here.](https://life-in-numbers-8fabeba9f5dd.herokuapp.com/)<br>

 *Your Life in Numbers* is a command-line interface program whose main goal is to provide the user with some facts based on the user's age, gender(GAAB/Current physical sex), height and weight. Upon receiving the user's input, the application presents/calculates the specified information regarding the chosen topic. Subsequently, the user has the option to either switch to the other topic, or exit the application. 

![Screenshot of the preview of application](documentation/readme/preview_life-in-numbers.png)<br>

## Table of contents

- [User Experience (UX)](#user-experience-(ux))
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

### User stories

*Your Life in Numbers* is for those who are interested in statistics about health topics and trivial facts around the age, weight and height of a human. 

As owner of the application:

- I want to build an application that allows users to learn more about their own BMI, their RMR (Resting Metabolic Rate) and some age-related topics. 
- I aim to ensure that the user interface remains consistent across all features to make it easy to use and navigate through.
- I want the application to provide clear instructions and have an intuitive design to ensure that the user receives all the information necessary for the correct use of the application.
- I expect the application to offer feedback to users during their interactions, guiding them through the input process.
- I would like to ensure the reliability of the application by implementing input validation mechanisms to avoid user errors and minimize the risk of technical problems or data inaccuracies.<br>

As visitor/user of the application:

- I want to easily understand what the purpose and the benefits of the program are.
- I want the application to provide clear instructions on how to use its features.
- I want the application to guide me through the process of entering my personal information, and expect the application to provide instant feedback to ensure that I provide accurate data.
- I want to know what my data is used for. 
- I want the interface to be visually appealing with concise explanations.
- I am keen to know more about some statistics and calculations around my life. 

## Design

- **Imagery:**<br>
  No images can be used in the terminal itself. The only way to display some kinds of pictures is by using ASCII Art. I created the logo for _Your Life in Numbers_  by using the font "Small Keyboard" with this [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Small%20Keyboard&t=Type%20Something%20) that creates ASCII Art from text.<br>

  ![Logo for Your Life in Numbers](documentation/readme_features/logo_life-in-numbers.png)<br>

  The background image was selected as a contrast to the terminal. The arrangement of the numbers in a spiral-like pattern makes it a perfect match for the subject of the application. 

- **Colour Scheme:**<br>
  The colour choices were limited, since this application is terminal-based. My main goal with my colour scheme was therefore to provide feedback to the user and give the application some structure and consistency. To add the colours for the project, I used [Python Colorama](https://pypi.org/project/colorama/)
 I made the following colour selection from Colorama:

  - GREEN <br>
  ![green validation screenshot](documentation/readme/green_life-in-numbers.png) <br>
  >  **Green** is the color most commonly associated with nature, **life**, **health**, youth, spring, hope, and envy. _(Wikipedia)_

  I used green for the logo of the application because it covers the topics of life and health. 
  Furthermore, it was used to show a positive message after a correct input by the user. <br>
  
  - RED <br>
  ![red validation screenshot](documentation/readme/red_life-in-numbers.png) <br>
  > Since **red** is the color of blood, it has historically been associated with sacrifice, **danger**, and courage. _(Wikipedia)_

  Red was used to display a negative message, respectively a warning if the user's input was invalid. <br>

  - CYAN <br>
  ![cyan input screenshot](documentation/readme/cyan_life-in-numbers.png) <br>
  > **Cyan** [...] is typically associated with liveliness, youth and **energy**, [...]. _(Designs.ai)_

  Cyan was used to query the user input. Since it is the colour between blue and green, it was perfect for the user questions, which must be valid (green in the application). The user's response and the calculated numbers can then be seen in blue.

  - BLUE <br>
  ![blue input screenshot](documentation/readme/input_life-in-numbers.png) <br>
  ![blue numbers screenshot](documentation/readme/blue_calculated_nums_life-in-numbers.png) <br>
  > **Blue** [...] often symbolizes serenity, **stability**, inspiration, or **wisdom**. _(Wikipedia)_

  The blue colour indicates the user's response and the calculated numbers in the topics. 

  - MAGENTA <br>
  ![magenta disclaimer screenshot](documentation/readme/magenta_life-in-numbers.png) <br>
  ![magenta heading screenshot](documentation/readme/heading_life-in-numbers.png) <br>
  > It _[**Magenta**]_ promotes compassion, support and kindness and encourages a sense of self-respect and contentment in those who use it. Physiologically magenta helps us to flow with life and let go of old ideas. It's associated with love, warmth and respect [...]. _(AZDESIGN)_

  Since data security is crucial to me, I used Magenta for the Disclaimer. It was also used for the headings of the topics. 

  - YELLOW <br>
  ![yellow subheadings screenshot](documentation/readme/yellow_life-in-numbers.png) <br>
  ![lightyellow heading screenshot](documentation/readme/light_yellow_life-in-numbers.png) <br>

  > **Yellow** is the colour people most often associate with amusement, **gentleness**, humor, **happiness**, and spontaneity [...]. _(Wikipedia)_
  
  Subheadings were labelled with yellow. The lighter version of yellow was used for the headline "ATTENTION" or the gender question. 

  - BLACK & WHITE <br>
   The Terminal is adorned with a black background and white text, except for the statements mentioned above. 

<details>
<summary> Click here to see the colour palette </summary>
<br>

The colour code for the colours in the terminal was taken by using the pipette function of [ColorZilla](https://www.colorzilla.com/de/chrome/welcome/new/?chrome/121.0.0.0/-/4.0). I created the colour palette with [coloors](https://coolors.co/).<br>
![Colour palette 1](documentation/readme/coloor_life-in-numbers-1.png)<br>
![Colour palette 2](documentation/readme/coloors_life-in-numbers-2.png)<br>

</details>

### Flowchart

The flowchart was crafted during the planning phase of the project and was created with [Lucid](https://lucid.app/). It still displays a third topic (Food/Drinks), that I would love to implement in the future. Furthermore, it has some additional input (smoking/alcohol) that I didn't use in the end. This could be a future enhancement.
<details>
<summary> Click here to see the flowchart </summary>
<br>

![Flowchart](documentation/readme/flowchart_life-in-numbers.png)

</details>

## Features

### Existing Features

To learn more about each feature, please click on the respective headline

<details>
<summary> Logo 'Your Life in Numbers' </summary>
<br>

The logo for the application was created with an [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Small%20Keyboard&t=Type%20Something%20) (Font: Small Keyboard).
Unfortunately, the ASCII Art created a warning of "invalid escape sequence". To resolve this issue, I used a blog post by [Adam Johnson](https://adamj.eu/tech/2022/11/04/why-does-python-deprecationwarning-invalid-escape-sequence/).<br>
![Screenshot Logo](documentation/readme_features/logo_life-in-numbers.png)<br>
The logo was designed for the welcome panel and is displayed again each time the application deletes the terminal from the previous entries. Only the ending of the app is an exception. 

</details>

<details>
<summary> Disclaimer </summary>
<br>

The disclaimer outlines the data management process of the application. It assures users that their data is stored temporarily during the program's use in a Google spreadsheet but will be deleted automatically once the program is exited correctly. Since the data that the user must provide to run the application properly is sensitive, the program seeks user confirmation to proceed, giving them the option to continue or decline. <br>
![Screenshot of the disclaimer](documentation/readme_features/disclaimer_life-in-numbers.png)<br>
If the confirmation is negated, the program is immediately terminated.<br>
![Screenshot of disclaimer termination](documentation/readme_features/disclaimer_no.png)<br>
When a user fails to respond and clicks "Enter" immediately, or types a number or a letter other than y or n, an error message appears, indicating that only y or n can be entered.<br>
![Screenshot of input errors in the dislaimer](documentation/readme_features/disclaimer_errors_life-in-numbers.png)
</details>

<details>
<summary> Google Spreadsheet </summary>
<br>

As soon as a user confirms the disclaimer, the existing worksheet 'user' is copied into the Google spreadsheet 'life-in-numbers-secure'. (See also: _Existing feature_ > _Input Validation_ > _1. Disclaimer_) Sensitive data should not normally be stored in a worksheet. Currently, however, the use of external databases is still beyond my capabilities. I therefore decided to use this method of copying and automatic deletion. 

![Google Spreadsheet with worksheet user](documentation/readme_features/user_worksheet_life-in-numbers.png)<br>

In order for the worksheet to be uniquely assigned to the user, the new worksheet is given a non-recurring name by adding a time stamp to it. 

![Google unique worksheet](documentation/readme_features/unique_worksheet_life-in-numbers.png)<br>

All data entered by the user is stored in this new created worksheet.(See also: _Existing Features_ > _Input Validation_ > _6. Weight_) This sheet also contains the age, which was calculated during the input display. The program uses this cell (f2) in later calculations and outputs for the topic _Trivia_. (see also: _Existing Features_ > _Topic TRIVIA_)

![Google unique worksheet with entries](documentation/readme_features/entries_worksheet_life-in-numbers.png)<br>

If the program is terminated properly, this unique worksheet is automatically deleted.(See also: _Existing Feature_ > _Input Validation_ > _7. Topic question_) <br>
![Video of exit in topics](documentation/readme_features/worksheet_delete_topic_exit.gif)
The user is informed at the very beginning that the application must be terminated properly to delete this data sheet. In the future, I would like to create a batch clean-up for abandoned worksheets if an error occurs or the user does not end the program properly.

**Notice:** A previous version of this README contained a link to the Google spreadsheet. I realised that this link was on a public repository and the spreadsheet may contain sensitive information. I deleted this link and switched in the code to a new hidden spreadsheet because the original link is still in my commit history. Many of the screenshots in the README are still with the old version of the spreadsheet, but the functionality is the same with the new version as well. 

</details>

<details>
<summary> Input Validation </summary>
<br>

In the course of the application, there are various inputs that the user must make. Since this involves different types of data, such as year of birth, name or weight, the validations also had to be adapted accordingly. 

1. **Disclaimer** (y/n) <br>
The first input validation can also be seen in the existing feature _Disclaimer_. The program requires user confirmation at the beginning before proceeding, giving them the option of continuing by typing _y_ or declining by entering _n_. An error message appears if a user does not answer and clicks 'enter' immediately or types a number or a letter other than _y_ or _n_.<br>
![Screenshot of input errors in the dislaimer](documentation/readme_features/disclaimer_errors_life-in-numbers.png)<br>
If a user refuses to consent, the program will be terminated immediately within a few seconds. <br>
![Screenshot of disclaimer termination](documentation/readme_features/disclaimer_no.png)<br>
As soon as the user agrees to the conditions by entering _y_, a new unique worksheet is created and the query of the data begins.<br>
![Gif of correct input in the dislaimer](documentation/readme_features/disclaimer_yes_new_worksheet.gif)<br>

2. **Name**<br> 
The user must make an entry, but this entry should not exceed 15 characters and must not contain special characters, numbers, or spaces.
![Screenshot incorrect input for name](documentation/readme_features/name_incorrect_input.png)<br>
If the name does not start with a capital letter, it is automatically capitalized by the program (see blue name in the greeting)<br>
![Screenshot of correct name input](documentation/readme_features/name_input_correct.png)<br>

3. **Birth year**<br>
The user must make an entry. The year of birth should not contain spaces or letters and must be exactly 4 numbers long. In addition, the year of birth must be within a reasonable range. As a guideline, the current year and the oldest person according to Guinness World Record was used here as limitation.<br>
![Screenshot of valid input birth year](documentation/readme_features/birth_year_incorrect_input.png)<br>
As soon as the user enters a year of birth within the permitted range, it is confirmed and the screen is cleared.
![Screenshot of valid input birth year](documentation/readme_features/birth_year_valid_input.png)<br>

4. **Gender(GAAB/CPS)**<br>
The question of gender of the user is a particularly sensitive one. I have therefore included a note explaining that this statement must be made because some calculations are based on gender. I tried to explain that the limited options here are just due to the nature of the application, but that they are not meant to exclude or discriminate. <br>
![Screenshot of gender attention](documentation/readme_features/gender_attention.png)<br>
An error message appears if a user does not answer and clicks 'enter' immediately, types a number or a letter other than _f_ or _m_. <br>
![Screenshot of invalid input for gender](documentation/readme_features/gender_invalid_input.png)<br>
As soon as the user has typed _f_ or _m_, he receives a confirmation that this input can be used and the next question (height) is displayed. <br>
![Screenshot of valid input for gender](documentation/readme_features/gender_correct_input.png)<br>

5. **Height** <br>
The user must provide a height specification (with a point for decimal), which must be within a reasonable range (minimum is the average height of a newborn and maximum is the Guinness world record). Otherwise, an error message is displayed.<br>
![Screenshot of invalid input for height](documentation/readme_features/height_invalid_input.png)<br>
The next question (weight) is displayed after a valid entry is confirmed.
![Screenshot of valid input for height](documentation/readme_features/height_correct_input.png)<br>

**Notice:** Currently, height and weight are not validated against each other. This means that you can theoretically enter a valid height of 1.98 m and a valid weight of 3 kg. To integrate a function that performs this kind of validation sensibly, a detailed search is needed to find out which values are in a reasonable range. I would like to this for a future feature.

6. **Weight** <br>
The user must provide their weight (with a point for decimal), which must be within a reasonable range (minimum is the average height of a newborn and maximum is the Guinness world record). Otherwise, an error message is displayed.
![Screenshot of invalid input for weight](documentation/readme_features/weight_invalid_input.png)<br>
As soon as the user has made a valid entry, a positive confirmation is displayed and in the background, the worksheet is automatically updated.<br>
![Video of valid input for weight](documentation/readme_features/weight_input_worksheet.gif)<br>

**Notice:** Currently, height and weight are not validated against each other. This means that you can theoretically enter a valid height of 1.98 m and a valid weight of 3 kg. To integrate a function that performs this kind of validation sensibly, a detailed search is needed to find out which values are in a reasonable range. I would like to this for a future feature.

7. **Topic question** <br>
After all data has been entered correctly and the worksheet has been updated, the user is shown the possible topics. <br>
![Screenshot of of the topic question](documentation/readme_features/topics.png)<br>
An error message appears if a user does not answer and clicks 'enter' immediately, types a letter or a number other than _1_, _2_ or _3_.<br>
![Screenshot of invalid input for the topic question](documentation/readme_features/topics_invalid_input.png)<br>
At this point, it is possible to exit the application and delete the data from the spreadsheet. <br>
![Video of exit in topics](documentation/readme_features/worksheet_delete_topic_exit.gif)

8. **Other topic question (y/n)** <br>
After the user has decided on a topic, he is asked if he also wants to learn something about the other topic. Again, he has the opportunity to end the program. <br>
An error message appears if a user does not answer and clicks 'enter' immediately, types a letter or a number other than _y_ or _n_.<br>
![Screenshot of invalid input for the topic question](documentation/readme_features/invalid_input_next-topic.png)<br>
When the user enters _n_, a short farewell message is displayed in which the user’s name is used. In addition, the screen is cleared after 5 seconds and the worksheet is deleted.<br>
![Video of exit in next topics](documentation/readme_features/next_topic_no.gif)
</details>

<details>
<summary> Display of the entered data </summary>
<br>

After the user has entered all the data correctly and the worksheet has been updated, the user will be shown his entries again. The data from the worksheet is used for this purpose. 
At this point, I would like to include in the future the possibility that the user can change their data again. <br>
![Video of displaying data to user](documentation/readme_features/worksheet_update.gif)<br>

</details>

<details>
<summary> Topic HEALTH </summary>
<br>

If the user has selected the topic _Health_ by pressing 1 in the topic question (see also: _Existing Feature_ > _Input validation_ > _7. Topic question_), the screen is deleted, and the logo is displayed again. Then the BMI, the life expectancy in weeks and finally the RMR is shown. The calculated numbers are displayed in blue. After the calculations, the user has the option to either quit the program or learn about the other topic _Trivia_<br>
![Video of displaying the topic health to user](documentation/readme_features/health_topic.gif)<br>
While I was writing the README, I noticed that in the second function for the topic _Health_, I did not use parameters, but only variables. So I created a test python file to see if the code will still work correct if I insert the parameters. After doing this successfully, I copied the entire code from the test file and replaced the existing code so as not to forget a value. I know that this is clearly not best practice because, of course, the commits for this step can no longer be traced well. I have therefore decided to mention this here, at least in the README. Nevertheless, now the class User is used uniformly for all parameters in the function health. 

1. **BMI** <br>
Body Mass Index (BMI) is a person's weight in kilograms divided by the square of height in meters. The grading within the individual classes(e.g. underweight, normal weight etc.) according to gender was taken from a German blog: [Rezeptrechner](https://www.rezeptrechner-online.de/blog/bmi-tabelle-rechner/) The calculator can exclusively be used for adults, 20 years old and older. The BMI for children and teens is slightly different and is given in percentiles. I would like to add this feature in the future.<br>

2. **Years and Weeks** <br>
The average life expectancy of men and women was found on the [database earth](https://database.earth/population/europe/life-expectancy). These numbers and the age of the user are the basis for the calculations carried out at this point. <br>

3. **RMR** <br>
The Resting Metabolic Rate(RMR) was calculated with the Mifflin-St Jeor Equation: <br>
Men: (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5. <br>
Women: (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161. <br>
It was found at the [NASM Blog](https://blog.nasm.org/nutrition/resting-metabolic-rate-how-to-calculate-and-improve-yours). I could not assign a variable to the given numbers(e.g. 10, 6.25) because I did not find the exact assignment they represent.

</details>

<details>
<summary> Topic TRIVIA </summary>
<br>

If the user has selected the topic _Trivia_ by pressing 2 in the topic question (see also: _Existing Feature_ > _Input validation_ > _7. Topic question_), the screen is deleted, and the logo is displayed again. After that, a birthday greeting, age in dog years and age on different planets will be displayed. The calculated numbers are displayed in blue. After the calculations, the user  has the option to either quit the program or learn about the other topic _Health_.<br>
![Video of displaying the topic trivia to user](documentation/readme_features/topic_trivia.gif)<br>

To perform the calculations for the topic _Trivia_, a variable was created, which refers to the value 'Age' from the worksheet. This should show that I can also use concrete data from the spreadsheet.<br>

1. **Happy Birthday** <br>
This is a simple birthday greeting. <br>

2. **Dog Years**<br>
How to calculate a human's age into dog years was found at the website of the [American Kennell Club](https://www.akc.org/expert-advice/health/how-to-calculate-dog-years-to-human-years/). As a general guideline, it can be broken down like this:<br>
> - 15 human years equals the first year of a medium-sized dog’s life. <br>
> - Year two for a dog equals about nine years for a human. <br>
> - And after that, each human year would be approximately five years for a dog. _(American Kennell Club)_ <br>

3. **Celestial Age**<br>
This section calculates the age that the user would have on another planet of our solar system, depending on the amount of time it takes this planet to make one trip around the sun.<br>
The exact calculation was found at [girlstart](https://girlstart.org/wp-content/uploads/2017/07/13.Age-on-Planets.pdf) and can be broken down like this:
- Multiply the age of the user by 365 (How long it takes for the Earth to orbit the Sun)
- Divide the age in Earth days by the number of days in a planet’s year (orbital period).

</details>

<details>
<summary> Program ending </summary>
<br>

The end of the program can be initiated at various points. Every time a user ends the application, the corresponding worksheet will be deleted permanently.(see also: _Existing Features_ > _Google Spreadsheet_) <br>
The first time, the program can be terminated after the disclaimer was displayed (see also: _Existing Features_ > _Disclaimer_). The next exit point is after the correct entry of all data when the topics are displayed (see also: _Existing Features_ > _Input validation_ > _7. Topic question_). After selecting one of the topics (either _Health_ or _Trivia_), you can exit the application as well (see also: _Existing Features_ > _Input validation_ > _8. Other topic question_). The final ending is the display of the second topic. Here, you only have to press Enter to quit the application.  <br>
![Video of the end of the application](documentation/readme_features/end_of_application.gif)

</details>

### Features, which I would like to implement in the future

- I want to implement a login option so that the user can create an account and return to the application to view and update their data. 
- I would like to create more topics, like food/drinks. In this category, you could find some information about the average consumption of certain foods(e.g. vegetables, meat, etc.) per life or year.
- I want to add some input requirements for habits such as smoking or alcohol consumption. This data could be used to adjust some of the calculations, such as life expectancy. In addition, the application could show how a change in this habit would be noticeable in the numbers. 
- I intend to add a batch clean-up of abandoned worksheets (e.g. every night at 1pm or once a week at 12am). Because right now, I have to regularly check if a user didn't end the application properly or an error has occurred, and the spreadsheet still contains abandoned worksheets. 
- I would like to add the BMI equivalent for people under 19. 
- I would like to include an additional validation that considers the ratio of height and weight. 

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)/ [CSS](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used to save and store the files for the website.
- [Heroku](https://www.heroku.com) was used to deploy the application.
- [VS Code](https://code.visualstudio.com/) was used as IDE. 
- [Lucid](https://lucid.app/) was used to create the Flowchart.
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) to beautify the code
- [LanguageTool](https://languagetool.org/) was used to check the grammar and spelling in the README and the Code. 
- [Coloors](https://coolors.co/image-picker) was used to create the color scheme.
- [Pixelied](https://pixelied.com/convert/jpg-converter/jpg-to-webp) was used to convert jpg images into wepb images.
- [Tinypng](https://tinypng.com/) was used to compress the webp background-image.
- [Pixabay](https://www.pixabay.com/de-de/) was used to search and load the background image.
- [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Small%20Keyboard&t=Type%20Something%20) was used to create the logo.
- [Google Spreadsheet](https://docs.google.com/spreadsheets/u/0/?pli=1) was used to create the worksheet for the application.
- [QuickTime Player](https://support.apple.com/en_GB/downloads/quicktime) was used to create for recording the screen.
- [xconvert](https://www.xconvert.com/) was used to convert the screen recording from mov into gif.
- [Browserling](https://www.browserling.com/) was used to test the application on different browsers.

**Libraries and modules used:** <br>
- [sys](https://docs.python.org/3/library/sys.html) was used to get system-specific functions like exit(). It was also necessary for the typing-print effect. 
- [time](https://docs.python.org/3/library/time.html) was used to access the sleep() function for the time delay.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) was used to get access to Google authentication. 
- [gspread](https://docs.gspread.org/en/v5.10.0/) was used for the Google sheets functionality 
- [datetime](https://docs.python.org/3/library/time.html) was used to get the current year and give the copied worksheets a time stamp in the name to make it unique. 
- [colorama](https://pypi.org/project/colorama/) was used to color the text in the terminal.

## Testing

1. **Validator Testing**

- **[CI Python Linter](https://pep8ci.herokuapp.com/#)**

  - result for run.py<br>
  In the first run I had some warnings about trailing whitespace and errors about too long lines, but after fixing those, no more errors were found. 
    ![Python linter result for run.py](documentation/readme/python-linter-ci-result.png)<br>

- **[HTML Validator](https://validator.w3.org/)**

  - result for layout.html<br>
  Since I added a favicon, a meta description, a title and some style to the layout.html file, I did check the layout.html file with the [Nu Html Checker](https://validator.w3.org/nu/about.html). In the first run, it came back with an error for the CSS height in the style area because I added a space between the number and the unit. After deleting this space, it came back with no errors or warnings. 
  ![HTML Validator result for layout.html](documentation/readme/html-validator_layout-life-in-numbers.png)<br>

2. **Lighthouse Test** <br>
   To measure the website against performance, accessibility, SEO and best practice, I used [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=de).<br>
   - result <br>
  Although I was told that we don’t have to do a Lighthouse test, I still created one for the site, as I added a background image, among other things. 
  The 94% were caused by the background image and the border of the "Run Program" button. I couldn’t improve accessibility further, but since this project wasn’t HTML/CSS first, I thought 94% was still a good result.
   ![Lighthouse](documentation/readme/lighthouse_life-in-numbers.png)

3. **Manual testing** <br>

| **Test** | **Test Description** | **Expected Outcome** | **Result** |
|:---|:---|:---|:---|
| Program start | Open the link for the live website or click on the _Run Program_ button | As soon as the page is loaded or the _Run Program_ button was clicked, the logo for the application and the Disclaimer should be displayed | Pass |
| Disclaimer - invalid input | Press _Enter_ key, type a number or a letter other than _y_ or _n_ and then press _Enter_ key | A warning/message that the user needs to make a correct input | Pass |
| Disclaimer - _n_ input | Type _n_ and press _Enter_ key | A farewell message is displayed, and the program exits by clearing the screen. | Pass |
| Disclaimer - _y_ input | Type _y_ and press _Enter_ key | A positive confirmation is displayed, and the program starts in the query of the data | Pass |
| Google Spreadsheet - new worksheet | Type _y_ and press _Enter_ | In the Google spreadsheet, the existing user worksheet should be copied and given a unique name. | Pass |
| Google Spreadsheet - delete worksheet | Go to the end of the application and confirm the exit. | The created worksheet should be deleted automatically. | Pass |
| Name question - invalid input | Press _Enter_ key, type a number, a space, a special character or a name longer than 15 characters and then press _Enter_ key | A warning/message that the user needs to make a correct input should be displayed | Pass |
| Name question - valid input | Type a name and press _Enter_ key | A positive confirmation should be shown and the next question (year of birth) should be displayed. | Pass |
| Birth year - invalid input | Press _Enter_ key, type a letter, a space, a special character, enter more or less than four numbers or an age outside a reasonable range.(-116 years-current year) and then press _Enter_ key | A warning/message that the user needs to make a correct input is shown | Pass |
| Birth year - valid input | Type four numbers in the reasonable range and press _Enter_ key | A positive confirmation should be shown, the terminal should be cleared and the note about gender should be displayed. | Pass |
| Gender - invalid input | Press _Enter_ key, type a letter other than f or m, a space, a special character and then press _Enter_ key| A warning/message that the user needs to make a correct input is shown | Pass |
| Gender - valid input | Type f or m and press _Enter_ key| A positive confirmation should be shown and the next question (height) should be displayed | Pass |
| Height - invalid input | Press _Enter_ key, type a letter, a space, enter the height with a comma for decimal or a height outside a reasonable range (0.49m-2.72m) and then press _Enter_ key | A warning/message that the user needs to make a correct input is shown | Pass |
| Height - valid input | Type the height inside the reasonable range with a point for decimal and press _Enter_ key| A positive confirmation should be shown and the next question (weight) should be displayed | Pass |
| Weight - invalid input | Press _Enter_ key, type a letter, a space, enter the weight with a comma for decimal or a weight outside a reasonable range (3.3kg-650.0kg) and then press _Enter_ key | A warning/message that the user needs to make a correct input is shown | Pass |
| Weight - valid input | Type the weight inside the reasonable range with a point for decimal and press _Enter_ key| A positive confirmation should be shown, and the worksheet should be updated | Pass |
| Display of entered data | Enter a valid weight and press the _Enter_ key | The data entered should be displayed to the user. | Pass |
| Topics question | Enter a valid weight and press the _Enter_ key | The data entered should be displayed to the user, then the screen is cleared, the logo is displayed again and the topics question is loaded | Pass |
| Topics question - invalid input | Press _Enter_ key, type a letter, a space or a number other than 1, 2 or 3 and then press _Enter_ key | A warning/message that the user needs to make a correct input is shown | Pass |
| Topics question - valid input: 1 | Type 1 and press _Enter_ key| The screen should clear and then the logo and topic _health_ should be displayed with BMI, life expectancy and RMR | Pass |
| Topics question - valid input: 2 | Type 2 and press _Enter_ key| The screen should clear and then the logo and topic _trivia_ should be displayed with Happy Birthday, dog years and celestial age | Pass |
| Topics question - valid input: 3 | Type 3 and press _Enter_ key| A farewell message should be displayed and the message that the program will quit in the next 5 seconds. At the same time, the worksheet should automatically delete itself. | Pass |
| Next topic question - invalid input | Press _Enter_ key, type a letter, a space or a number other than y or n and then press _Enter_ key | A warning/message that the user needs to make a correct input is shown | Pass |
| Next topic question - valid input: _y_ | Type _y_ and press _Enter_ key| The screen should clear and then the logo and the other topic should be displayed | Pass |
| Next topic question - valid input: _n_ | Type _n_ and press _Enter_ key| A farewell message should be displayed and the message that the program will quit in the next 5 seconds. At the same time, the worksheet should automatically delete itself. | Pass |
| Program ending | Press _Enter_ key after the second topic was displayed | Once the second topic has been displayed, a single sentence should be displayed, prompting the user to press enter. After pressing the _Enter_ key, the farewell message should be displayed and the message that the program will quit in the next 5 seconds. At the same time, the worksheet should automatically delete itself. | Pass |

4. **Browser Compatibility**<br>
  The tests were conducted using the following browsers:

- Google Chrome Version 121.0.6167.160
The following tests were conducted by using [browserling](https://www.browserling.com/)
- Edge Version 118
- Firefox 119
- Opera 104

I have tested the website on Safari on macOS Sonoma 14.3, but unfortunately, it just opens the website and starts the program, but I can’t enter any input.

5. **Bugs**

**Clearing the screen:**<br>
First I had implemented the following function to clear the screen:
```
    def clear_screen ():
        '''
        Clears the screen from text
        '''
        os.system('cls' if os.name == 'nt' else 'clear')
```

Unfortunately, this version did not delete the entire screen in the deployed version of the application(it did work properly in my IDE), but only the visible area. Parts of the logo were displayed twice when the screen emptied, as soon as the text was longer than the viewport. My mentor Brian Macheria then gave me a version with which the function worked smoothly:
```
    print("\033c", end="")
```
Initially, I had this version as a backup, but after another conversation with my mentor, I deleted the original version. 

**Typing-print statement in the weight/height validation:** <br>
When validating the input of size and weight, the typing-print statement: _"Your height/weight should be given in m/kg and contain a point for the decimal place."_ always appeared again if the user has given a value outside the reasonable range, but it should only appear once at the beginning. I could fix this by changing the position of this typing-print statement. 

**Duplicate the worksheet _user_** <br>
After I made the project available for code review in the Slack community of the Code Institute, I was told that the age calculation for the "Happy Birthday" message of a 104-year-old was apparently incorrect. After checking the corresponding function that worked as expected, I looked into the spreadsheet and found that someone clearly did not exit the application correctly. The still existing worksheet with the old data in it was then copied and not the _user_ worksheet. Since the functions of the trivia theme rely on a special cell(_F2_), only the value of this copied sheet (in this case with an age of 45) was used. I was able to fix this by referring to the worksheet’s name:
```
    WORKSHEET_USER = SHEET.worksheet('User')
```
 instead of the worksheet’s index:
 ```
    WORKSHEET_USER = SHEET.get_worksheet(0)
```

## Deployment

### Heroku
This site is deployed using Heroku. To deploy it from its GitHub repository to Heroku, I took the following steps:

1. Create a list of requirements in the requirements.txt file by using the command _pip3 freeze > requirements.txt_
2. Log in (or sign up) to Heroku
3. Click on the _New_ button and select _Create new app_
4. Give it a unique name and choose the region _Europe_
5. Click the *Settings* tab, go to the _Config Vars_ section and click on the _Reveal Config Vars_ button
6. Copy the content of the creds.json file() and paste it into the value field, then name the _Key_ CREDS, like the variable that holds the json file in the run.py file
7. Click the _Add_ button
8. Add a second key _PORT_ and set the value to _8000_
9. Go to the _Buildpacks_ section and click the _Add Buildpacks_ button
10. Select _python_ and click the _Save changes_ button
11. Add a second buildpack: _nodejs_
12. Click the *Deploy* tab, go to the _Deployment method_ section, select _GitHub_ and confirm this selection by clicking on the _Connect to Github_ button
13. Search for the repository name on github _life-in-numbers_ and click the _Connect_ button 
14. Enable the automatic deploy or manually deploy the code from the main branch.<br>

To see the [view of the live site](https://life-in-numbers-8fabeba9f5dd.herokuapp.com/) click on the _Open app_ button on the top right corner or, if you enabled automatic deploy(step 14), log in to GitHub, navigate to the repository for this project by selecting [*queenisabaer/life-in-numbers*](https://github.com/queenisabaer/life-in-numbers), click on _Deployment_ and choose in the _Environments_ section _life-in-numbers_. On top of the latest deployment is the link to the [live site](https://life-in-numbers-8fabeba9f5dd.herokuapp.com/).

### Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*queenisabaer/life-in-numbers*](https://github.com/queenisabaer/life-in-numbers)
3. Click at the top of the repository on the **Fork** button on the right side

### Clone this repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*queenisabaer/life-in-numbers*](https://github.com/queenisabaer/life-in-numbers)
3. In the top right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key

### Create a Google Spreadsheet(data model) and integrate it using API

*__Create the Google Spreadsheet__*
1. Log in (or sign up) to Google Account
2. Access [Google spreadsheet](https://docs.google.com/spreadsheets/u/0/?pli=1)
3. Create a new spreadsheet and give it a descriptive name, e.g. _'life-in-numers'_ like the name of the application
4. Rename the worksheet (e.g. _'user'_) and add, if neccessary, additional worksheets 
5. Add headings (_Name, Birth year, GAAB/CPS (m/f), Height in m, Weight in kg, Age_)<br>

*__Set up the APIs__*

1.  Navigate to the [Google Cloud Platform ](https://console.cloud.google.com/)
2. Create a new project by clicking the button _Select a project_ and then select _new project_<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![New Project Google Cloud](documentation/deployment/google_cloud_new_project.png)
    </details>
3. Give the project a descriptive and meaningful name, e.g. life-in-numbers and click on the _CREATE_ button<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Project Name Google Cloud](documentation/deployment/google_cloud_project_name.png)
    </details>
4. In the Notifcations pop-up, click on "SELECT PROJECT"<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Notification Google Cloud](documentation/deployment/google_cloud_notification.png)
    </details>
5. On the project page go to the menu (click the burger icon in the top-left corner of the page), click on _APIs and services_ and then select _Library_<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Library selection Google Cloud](documentation/deployment/google_cloud_library.png)
    </details>
6. In the search bar, search for _Google Drive_ and enable it<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google cloud search bar for Google Drive API](documentation/deployment/google_cloud_google_drive_API.png)<br>
    ![Google Drive API enable button](documentation/deployment/google_cloud_enable.png)
    </details>
7. To connect to this API, you need to generate CREDENTIALS (proof to the Google Drive, that you have permission to access) by clicking on _Credentials_ in the sidebar and then select _+ CREATE CREDENTIALS_ > _Help me choose_
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API Credentials](documentation/deployment/google_cloud_credentials.png)<br>
    ![Google Drive API create Credentials](documentation/deployment/google_cloud_create_credentials_service.png)
    </details>
8. In the _Credential Type_ section, select _Google Drive API_ and Application Data and click on the _NEXT_ button<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API credential type](documentation/deployment/google_cloud_credentials_type.png)
    </details>
9. Enter a costume service name and click the _CREATE AND CONTINUE_ button<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API account name](documentation/deployment/google_cloud_service_account.png)
    </details>
10. As role, select _Editor_ in the Quick access section _Basic_ and press the _CONTINUE_ button<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API Role](documentation/deployment/google_cloud_role.png)<br>
    ![Google Drive API Role2](documentation/deployment/google_cloud_role2.png)
    </details>
11. The form fields in the next question: _Grant users access to this service account_ can be left blank, just click on the _DONE_ button<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API acess user blank](documentation/deployment/google_cloud_acess_blank.png)
    </details>
12. Click on the mail from the new created Service Account<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API service acoount mail](documentation/deployment/google_cloud_service_mail.png)<br>
    </details>
13. Click on the Tab _KEYS_ and then select _Create new key_ from the dropdown menu of the _ADD KEY_ button<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API service acoount mail](documentation/deployment/google_cloud_keys.png)
    </details>
14. The key type can stay as JSON, just click the _CREATE_ button. Then a json file will be downloaded in to your local maschine.<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API service acoount mail](documentation/deployment/google_cloud_key_type.png)
    </details>
15. Make sure that the json file is never committed to GitHub, since it contains sensitive information. For this purpose, create a _.gitignore_ file in the workspace and add the name of the json file to it.
16. Go back to the library again (Step 5) and search for _google sheets api_ and enable it<br>
    <details>
    <summary> View this step as screenshot</summary>
    <br>

    ![Google Drive API service acoount mail](documentation/deployment/google_cloud_google_sheet.png)<br>
    ![Google Drive API service acoount mail](documentation/deployment/google_cloud_google_sheet_enable.png)
    </details>
17. Drag and drop the credential-json file, that was downloaded after step 14, into the workspace and rename it as _creds.json_(for simplicity reasons)
18. Open the json file in the workspace and copy the _client mail_ without the quotes
19. Go to the created Google Spreadsheet and click the _Share_ button
20. Paste in the mail adress (step 17), select _Editor_ and then click _Share_

*__Connecting the APIs to Python__*
1. In the workspace terminal command 'pip3 install gspread google-auth'.  
2. Import the gspread library on top of the python file in the workspace. 
3. Then import the _Credentials_ from the Google Auth Account (google.oauth2.service_account)
4. Set the _SCOPE_, that lists the APIs, the program needs to access to run.
5. Create _CREDS_, use the gspread authorize method and access the created worksheet data


## Credits

### Content

- The background image is from [Pixabay by Gerd Altmann](https://pixabay.com/de/illustrations/zahlen-nummern-unendlichkeit-937884/).
- The average weight and height of a human baby was found [here](https://www.sueddeutsche.de/gesundheit/geburtsgroesse-das-neue-standardbaby-1.2124509), which includes this study from [the lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(14)61490-2/abstract).
- The [heaviest](https://en.wikipedia.org/wiki/List_of_heaviest_people) and [tallest](https://en.wikipedia.org/wiki/List_of_tallest_people) person were found on a list on [Wikipedia](https://en.wikipedia.org/wiki/Main_Page).
- The classification for the BMI was taken from [this site](https://www.rezeptrechner-online.de/blog/tag/bmi-tabelle-teenager/).
- The numbers for life expectancy in Europe was found on the [database earth](https://database.earth/population/europe/life-expectancy).
- How to calculate the Resting Metabolic Rate was found [here](https://blog.nasm.org/nutrition/resting-metabolic-rate-how-to-calculate-and-improve-yours).
- How to calculate human years into dog years was found at [American Kennel Club](https://www.akc.org/expert-advice/health/how-to-calculate-dog-years-to-human-years/).
- Examples of sidereal periods for the planets were found at [Wikipedia](https://en.wikipedia.org/wiki/Orbital_period).
- How to calculate the personal age on another planet was from a PDF chart at [girlstart](https://girlstart.org/wp-content/uploads/2017/07/13.Age-on-Planets.pdf).

### Code

- To import the gspread library, set the APIs, update the worksheet and get the data from this worksheet, I used the walkthrough project *love-sandwich* from Code Institute. 
- Although I didn't use this function in the end (but can still be seen on the early versions on GitHub commits), I want to mention that I used a thread on GitHub by [Anton Burnashev](https://github.com/burnash/gspread/issues/387) to create a function that clears parts of the Google worksheet. 
- To learn more about the usage of gspread I read articels by [Anton Burnashev](https://docs.gspread.org/en/latest/user-guide.html), by [Sogo Sogo Ogundowole](https://medium.com/hacktive-devs/gspread-automate-google-sheet-with-python-dc1fa7c65c21) and blogposts at [Codeforests](https://www.codeforests.com/2020/11/22/gspread-read-write-google-sheet/)
- To duplicate an existing worksheet, I found [this thread on GitHub](https://github.com/burnash/gspread/issues/452) helpful. 
- How to clear the screen was found in an article by [altcademy](https://www.altcademy.com/blog/how-to-clear-screen-in-python/), in the end I only used another print statement, that was given me by my mentor Brian Macheria. 
- To create a typewriting effect, I used the tutorial by [101computing](https://www.101computing.net/python-typing-text-effect/)
- To learn more about the idiom: if__name__ == "__main__", I read this [article by Martin Breuss](https://realpython.com/if-name-main-python/).
- How to use the zip method to combine two lists was found on [Stack Overflow](https://stackoverflow.com/questions/71086453/how-to-combine-the-elements-of-two-lists-using-zip-function-in-python)
- How to wait for a pressed key was found at [Stack Overflow](https://stackoverflow.com/questions/983354/how-do-i-wait-for-a-pressed-key)
- To understand more about the concepts of Python, I used the Udemy course: [100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu](https://www.udemy.com/course/100-days-of-code/)
- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [mdn](https://developer.mozilla.org/en-US/)
  - [W3C](https://www.w3.org/)
  - [W3schools](https://www.w3schools.com/)
  - [DevDocs](https://devdocs.io/)
  - [Stack Overflow](https://stackoverflow.com/)
  - Slack Community

### Media

- To understand more about Colorama I watched the tutorial by [Tech with Tim](https://www.youtube.com/watch?v=u51Zjlnui4Y)

### ReadMe

- Still, a big thank you to [Kera Cudmore](https://github.com/kera-cudmore) and all of her tips on what makes a good README.

### Acknowledgments

- I would like to thank my amazing mentor Brian Macheria for his numerous tips and wonderful assistance during the creation of this project. 
- I would also like to thank Gary Dolan for his great project [Pokémon Portfolio](https://github.com/GaryDolan/ci-p3-pokemon-portfolio/blob/main/README.md). It helped me a lot to style the background and the terminal. 
- Furthermore, I would like to thank Niclas Hugdahl, who tested my code extensively and drew my attention to the error with the worksheet.

**This is for educational use.**

# Your Life in Numbers

Python Essentials Project Portfolio - Code Institute_

View deployed site [here.](https://queenisabaer.github.io/life-in-letters/)

 *Your Life in numbers* is a command-line interface program whose main goal is to provide the user with some facts based on the user's age, sex, height, weight and habits. Upon receiving the user's input, the application presents/calculates the specified information reagrding the chosen topic. Subsequently, the user has the option to either persist with the chosen feature, switch to another feature, or exit the application. 

![Responsive Mockup](documentation/)

## Table of contents

- [User Experience (UX)](#user-experience)
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

### User stories

-  *Your Life in numbers* is for those who are interested in statistics about life expectancy, health topics and trivial facts around the age of a human. 

## Design

- **Imagery:**
  xxx
- **Colour Scheme:**
  xxx <br>

- **Typography:**
  xxx

### Flowcharts

<details>
<summary> xxx </summary>
<br>

![Flowchart](documentation/)

</details>

## Features

### Existing Features

The ASCII Art created a warning of "invalid escape sequence". To fix this issue I used a blog post by [Adam Johnson](https://adamj.eu/tech/2022/11/04/why-does-python-deprecationwarning-invalid-escape-sequence/)


<details>
<summary> Screenshot x </summary>
<br>

![Screenshot](documentation/)
</details>

### Features, which I would like to implement in the future

- 

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used to save and store the files for the website.
- [Lucid](https://lucid.app/) was used to create the Flowchart.
- [CSS Gradient](https://cssgradient.io/) was used to create the gradient background of the instruction button
- [Am I Responsive](https://ui.dev/amiresponsive) was used to display the website on different devices.
- [beautifier](https://beautifier.io/) to beautify the code
- [LanguageTool](https://languagetool.org/) was used to check the grammar and spelling in the README. 
- [Colorama](https://pypi.org/project/colorama/)was used to color the text in the terminal.
- [Pixelied](https://pixelied.com/convert/jpg-converter/jpg-to-webp) was used to convert jpg images into wepb images.
- [Tinypng](https://tinypng.com/) was used to compress the webp background-image.

## Testing

1. **Validator Testing**

- **[CI Python Linter](https://pep8ci.herokuapp.com/#)**

  - result for run.py<br>
  In the first run I had some warnings about trailing whitespace and errors about too long lines, but after fixing those  no more errors were found. 
    ![result for run.py](documentation/readme/python-linter-ci-result.png)<br>
   
I also checked the page in the validator via text-input, and likewise no errors were detected in this way. All I got was information to avoid trailing slashes in void elements.

2. **Lighthouse Test** <br>
   To measure the website against performance, accessibility, SEO and best practice, I used [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=de).<br>
   - result for index.html<br>
   First, it gave a warning that the form element did not have the correct associated label. 
   ![Lighthouse]()

3. **Manual testing** <br>
To ensure the pages are responsive, I used the Google Chrome developer tools.

| **Test** | **Test Description** | **Expected Outcome** | **Result**|
|:---|:---|:---|:---|



4. **Browser Compatibility**<br>
  The tests were conducted using the following browsers:

- Google Chrome Version 120.0.6099.129
- Safari on Mac Version 17.0 (17616.1.27.111.22, 17616) 
- Safari on iOS 17.2.1
- Edge Version 120.0.2210.61

5. **Bugs**

- 

## Deployment NEEDS TO BE UPDATED AT THE END!!!

This site is deployed using Heroku. To deploy it from its GitHub repository to Heroku, I took the following steps:
1. Log in (or sign up) to GitHub.
2. Navigate to the repository for this project by selecting [*queenisabaer/life-in-numbers*](https://github.com/queenisabaer/life-in-numbers)
3. Click the *Settings* tab above the repository 
4. xxx
5. In the section **"xxx"** under *xxx* select *xxx* 
6. In the section **"xxx"** under *xxx* select in the first area *xx* and in the second *xxx*
7. Click the *Save* Button<br>
After refreshing the settings site for this repository above the **"Build and deployment"** section, you will see the Link to the Heroku Pages area with the link to the [view of the live site](https://queenisabaer.github.io/life-in-numbers/)

- Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*queenisabaer/life-in-numbers*](https://github.com/queenisabaer/life-in-numbers)
3. Click at the top of the repository on the **Fork** button on the right side

- Clone this repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*queenisabaer/life-in-numbers*](https://github.com/queenisabaer/life-in-numbers)
3. In the top right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key

## Credits

### Content

- The background image is from [pixabay by Gerd Altmann](https://pixabay.com/de/illustrations/zahlen-nummern-unendlichkeit-937884/)
- The average weight and height of a human baby was found [here](https://www.sueddeutsche.de/gesundheit/geburtsgroesse-das-neue-standardbaby-1.2124509), which includes this study from [the lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(14)61490-2/abstract)
- The heaviest and tallest person were found on a list in [wikipedia](https://en.wikipedia.org/wiki/List_of_heaviest_people)
- The classificatioon for the bmi was taken from [this site](https://www.rezeptrechner-online.de/blog/tag/bmi-tabelle-teenager/)
- The numbers for life expactancy in europe was found at the [database earth](https://database.earth/population/europe/life-expectancy)
- How to calculate the Resting Metabolic Rate was found [here](https://blog.nasm.org/nutrition/resting-metabolic-rate-how-to-calculate-and-improve-yours)
- How to calculate human years into dog years was found at [American Kennel CLub](https://www.akc.org/expert-advice/health/how-to-calculate-dog-years-to-human-years/)
- Examples of sidereal periods for the planets were found at [wikipedia](https://en.wikipedia.org/wiki/Orbital_period)
- How to calculate the personal age on another planet was from a pdf chart at [girlsstart](https://girlstart.org/wp-content/uploads/2017/07/13.Age-on-Planets.pdf)

### Code

- To import the gspread library, setting the APIs, update the worksheet and getting the data from this worksheet, I used the walkthrough project *love-sandwich* from Code Institute. 
- How to clear the screen was found in an article by [altcademy](https://www.altcademy.com/blog/how-to-clear-screen-in-python/)
- To create a typewriting effect I used the tutorial by [101computing](https://www.101computing.net/python-typing-text-effect/)
- Although I didn't use this function in the end(but can still be seen on the easrly versions on github), I want to mention that I used a thread on github by [Anton Burnashev](https://github.com/burnash/gspread/issues/387) to create a function that clears parts of the google worksheet. 
- To learn more about the if__name__ == "__main__" idiom, I read this [article by Martin Breuss](https://realpython.com/if-name-main-python/).
- To learn more about the usage of gspread I read [some articels by Anton Burnashev](https://docs.gspread.org/en/latest/user-guide.html)
- How to use the zip method to combine two lists was found on [Stack Overflow](https://stackoverflow.com/questions/71086453/how-to-combine-the-elements-of-two-lists-using-zip-function-in-python)
- How do I wait for a pressed key was found at [Stack Overflow](https://stackoverflow.com/questions/983354/how-do-i-wait-for-a-pressed-key)
- To understand more about the concepts of Python, I used the Udemy course: [The complete 2023 Web Development Bootcamp by Dr. Angela Yu](https://www.udemy.com/course/the-complete-web-development-bootcamp/)
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

- Still a big thank you to [Kera Cudmore](https://github.com/kera-cudmore) and all of her tips on what makes a good README.

### Acknowledgments

- I would like to thank my wonderful mentor Brian Macheria for his numerous tips and great assistance during the creation of this project. 

**This is for educational use.**
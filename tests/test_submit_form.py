from selene import have
from selene.support.shared import browser
import os

def test_submit_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('enchik')
    browser.element('#lastName').type('enchikov')
    browser.element('#userEmail').type('ivanov@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('8800555353')
    browser.element('#dateOfBirthInput').click()
    browser.element('option[value="6"]').click()
    browser.element('option[value="1992"]').click()
    browser.element('.react-datepicker__day--027').click()
    browser.element('#subjectsInput').type('English').press_tab()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath("../resources/original.jpg"))
    browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    browser.element('#currentAddress').type('Novosibirsk')
    browser.element('#state input').type('Rajasthan').press_tab()
    browser.element('#city input').type('Jaiselmer').press_tab()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
    browser.all("table tbody tr").should(have.exact_texts(
        'Student Name enchik enchikov',
        'Student Email ivanov@gmail.com',
        'Gender Male',
        'Mobile 8800555353',
        'Date of Birth 27 July,1992',
        'Subjects English',
        'Hobbies Music',
        'Picture original.jpg',
        'Address Novosibirsk',
        'State and City Rajasthan Jaiselmer'
    ))
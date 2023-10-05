Feature: Debt advice

    Scenario Outline: Visit the debt advice journey
        Given we visit the url <url>
        When we accept the cookies
        And we click the button to start the debt advice journey
        Then we should reach the first step of the tool with the title <title>

        Examples: Pages
            | url | title         |
            | /en | Your location |
            | /cy | Eich lleoliad |

    Scenario Outline: debt advice journey - England
        Given we visit the url <url>
        When we accept the cookies
        And we select <option_1_selector>
        Then the page title should be <expected_page_title>
        When we select <option_2_selector>
        Then we should see a link with the href <href>

        Examples: Pages
            | url        | option_1_selector       | expected_page_title | option_2_selector              | href                             |
            | /en/nation | button[value="England"] | Your employment     | button[form="formSubmission2"] | https://www.businessdebtline.org |
            | /cy/nation | button[value="Lloegr"]  | Eich cyflogaeth     | button[form="formSubmission2"] | https://www.businessdebtline.org |

    Scenario Outline: debt advice journey - Other
        Given we visit the url <url>
        When we accept the cookies
        And we select <option_1_selector>
        Then the page title should be <expected_page_title>
        Then we should see a link with the href <href>

        Examples: Pages
            | url        | option_1_selector        | expected_page_title        | href                                                                                   |
            | /en/nation | button[value="Scotland"] | Debt advice locator        | https://www.moneyhelper.org.uk/en/money-troubles/dealing-with-debt/debt-advice-locator |
            | /cy/nation | button[value="Cymru"]    | Lleolwr cyngor ar ddyledio | https://www.moneyhelper.org.uk/cy/money-troubles/dealing-with-debt/debt-advice-locator |

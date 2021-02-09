Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <middlename>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

Examples:
  | firstname  | lastname  | middlename  |
  | firstname1 | lastname1 | middlename1 |
  | Dmitriy    | Belkin    |             |

Scenario Outline: Delete contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Edit contact
Given a non-empty contact list
Given a random contact from the list
When I edit the contact with <firstname>, <lastname> and <middlename>
Then the new contact list is equal to the old list with the edited contact

Examples:
| firstname      | lastname      | middlename     |
| firstname1_new | lastname1_new | middlename_new |
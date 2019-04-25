@Agrostartest

Feature: Test order iphone.

@orderiphone
Scenario Outline: Order iphone x with specfication 256GB and Grey color
    Given navigates to amazon website
    And search apple <product>
    When open the <product> in new tab
    And add the product to cart
    And verify product is added to cart
    And proceed to buy the product
    And enter the credentails in the login page as '< username >' and '< password >'
    And enter the new shipping address
    Then verify navigaton to the delivery options page

    Examples:
    |product                                  |
    |apple iphone xs max 256gb - space grey   |
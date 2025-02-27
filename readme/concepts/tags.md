# Tags

Tags are a useful feature to organize and catalog utility consumption data in various custom and arbitrary ways. You can apply multiple tags to meters, virtual meters or meter groups. You can then analyze consumption data by tags. All meters that have the same tag will have their consumption data aggregated together. For example, if there are multiple tenants in a building and they each have mutiple meters, you can tag different meters or meter groups with the tenant name, and then analyze the consumption data based on the tenant name.

In order to provide structure and ensure data is clean, you need to pre-define your tags.

You start by defining a 'tag type' - for example 'Tenant'. You can then define multiple items under the 'Tenant' tag. You can add a tag for each tenant - 'ACME', 'Blueberry Electronics', 'Verper Stationary' etc..

What makes tags more interesting is that they can follow a hierarchial tree structure.

#### Tag Trees

You can define tags with parent and child tags. You can create tags and subtags and sub-sub tags and keep going on. The advantage of this is that when you want to analyze consumption data for a tag, it will automatically include all sub-tags (or child tags) as well. For example, if the 'Sunbucks Coffee' tenant has 2 different shops in a commercial building, you can define a tag structure for tenants like this:

* Tenant
  * Food and Beverage
    * Sunbucks Coffee
      * Ground Floor
      * 3rd Floor
    * Don Pepe

You can then tag the meters as either `Tenant/Food and Beverage/Sunbucks Coffee/Ground Floor` or `Tenant/Food and Beverage/Sunbucks Coffee/3rd Floor`.

You can either analyze data for each individual meter, or if you choose to analyze data for `Tenants/Food and Beverage/Sunbucks Coffee`, data from `Ground Floor` and `3rd Floor` will autoamtically be included in it.

If you analyze data for the tag `Tenant/Food and Beverage` it will also include consumption data from `Don Pepe` tagged meters as well.

Having a tree structure lets you segregate and analyze data individually or as a group.


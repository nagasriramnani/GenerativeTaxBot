import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.gov.uk/contact-official-receiver",
"https://www.gov.uk/late-commercial-payments-interest-debt-recovery/charging-interest-commercial-debt",
"https://www.gov.uk/get-help-hmrc-extra-support/if-you-need-someone-to-talk-to-hmrc-for-you",
"https://www.gov.uk/bankruptcy",
"https://www.gov.uk/marriage-allowance/how-to-apply",
"https://www.gov.uk/trusts-taxes",
"https://www.gov.uk/make-court-claim-for-money/work-out-interest",
"https://www.gov.uk/submit-vat-return/correct-errors-in-your-vat-return",
"https://www.gov.uk/tax-on-pension/how-your-tax-is-paid",
"https://www.gov.uk/government/organisations/hm-revenue-customs/contact/reporting-fraudulent-emails",
"https://www.gov.uk/importing-vehicles-into-the-uk/pay-vat-northern-ireland-eu",
"https://www.gov.uk/complain-to-hm-revenue-and-customs",
"https://www.gov.uk/capital-gains-tax/losses",
"https://www.gov.uk/respond-to-court-claim-for-money/pay-some-of-the-money",
"https://www.gov.uk/charge-reclaim-record-vat/vat-on-discounts-and-gifts",
"https://www.gov.uk/claiming-money-or-property-from-dissolved-company/restore-company-court-order",
"https://www.gov.uk/pay-vat/bank-or-building-society",
"https://www.gov.uk/capital-allowances/annual-investment-allowance",
"https://www.gov.uk/importing-vehicles-into-the-uk/paying-vat-and-duty",
"https://www.gov.uk/bankruptcy/your-income",
"https://www.gov.uk/national-insurance-credits",
"https://www.gov.uk/respond-to-court-claim-for-money",
"https://www.gov.uk/carers-credit",
"https://www.gov.uk/student-jobs-paying-tax",
"https://www.gov.uk/personal-tax-account",
"https://www.gov.uk/trusts-taxes/parental-trusts-for-children",
"https://www.gov.uk/tax-appeals/reasonable-excuses",
"https://www.gov.uk/tax-on-pension-death-benefits",
"https://www.gov.uk/capital-gains-tax-personal-possessions",
"https://www.gov.uk/tax-appeals/delay-payment",
"https://www.gov.uk/tax-company-benefits/national-insurance-on-company-benefits",
"https://www.gov.uk/applying-for-probate/fees",
"https://www.gov.uk/pay-self-assessment-tax-bill/bank-details",
"https://www.gov.uk/guidance/negligible-value-agreements",
"https://www.gov.uk/get-help-hmrc-extra-support/if-you-need-more-time-because-of-your-circumstances",
"https://www.gov.uk/vat-cash-accounting-scheme/join-or-leave-the-scheme",
"https://www.gov.uk/vat-charities",
"https://www.gov.uk/government/publications/asset-valuation-request-for-a-share-valuation-val230",
"https://www.gov.uk/debt-payments-from-your-wages/when-debt-paid-off",
"https://www.gov.uk/business-asset-disposal-relief/work-out-your-tax",
"https://www.gov.uk/self-assessment-tax-returns/corrections",
"https://www.gov.uk/county-court-judgments-ccj-for-debt/pay-the-judgment-if-you-do-owe-the-money",
"https://www.gov.uk/reduced-rate-election-payroll",
"https://www.gov.uk/tax-uk-income-live-abroad/selling-or-inheriting-assets",
]

output_file = "output.txt"

def scrape_content(url, div_id):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        div_content = soup.find('div', id=div_id)
        
        if div_content is None:
            print(f"Could not find div with id '{div_id}' on the URL: {url}")
            return None

        return div_content.get_text()
    else:
        print(f"Failed to fetch content from the URL: {url}. Status code: {response.status_code}")
        return None


with open(output_file, 'w', encoding='utf-8') as f:
    for url in urls:
        content = scrape_content(url, 'guide-contents')
        if content:
            f.write(content + '\n\n')
            print(f"Content from {url} written to {output_file}")
        else:
            print(f"Could not fetch content from {url}")

print(f"Scraping finished. Check the {output_file} for the extracted content.")

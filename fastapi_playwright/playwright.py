from playwright.async_api import async_playwright

async def save_page_content(url: str, output_path: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        content = await page.content()
        with open(output_path, 'w') as f:
            f.write(content)
        await browser.close()
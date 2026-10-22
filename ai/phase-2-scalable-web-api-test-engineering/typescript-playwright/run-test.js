const { chromium } = require('playwright');
(async () => {
  try {
    console.log('Launching browser...');
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    console.log('Navigating to login page...');
    await page.goto('https://the-internet.herokuapp.com/login');
    console.log('Page Title:', await page.title());
    await browser.close();
    console.log('Test completed successfully!');
  } catch (err) {
    console.error('Error:', err);
  }
})();

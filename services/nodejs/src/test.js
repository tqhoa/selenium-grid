const { Builder, By, Key, until } = require("selenium-webdriver");

async function googleSearch(browser) {
  let driver = await new Builder()
    .forBrowser(browser)
    .usingServer("http://selenium-hub:4444/wd/hub/")
    .build();

  try {
    // Navigate to Url
    await driver.get("https://www.facebook.com");
    // Enter text "Automation Bro" and perform keyboard action "Enter"
    await driver.findElement(By.name("q")).sendKeys("test", Key.ENTER);

    console.log(await (await driver.getCapabilities()).getBrowserName());
    console.log(await (await driver.getCapabilities()).getBrowserVersion());
  } finally {
    setTimeout(() => {
      driver.quit();
    }, 5000)
  }
}

//googleSearch('chrome')
for(let i = 1; i < 20; i++) {
  googleSearch('chrome');
}

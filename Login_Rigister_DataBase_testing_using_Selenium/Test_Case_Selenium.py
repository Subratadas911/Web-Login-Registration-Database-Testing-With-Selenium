package celeniumtest;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class firsttest {
public static void main(String[] args) throws InterruptedException {
System.setProperty("webdriver.chrome.driver", 
"C:\\selenium\\chromedriver.exe");
 WebDriver driver = new ChromeDriver();
 driver.get("http://localhost/Web_Project_Fall-main/Web_Project_Fall_main/completeProjectUser3/registration.php");
 driver.manage().window().maximize();
 driver.findElement(By.id("fname")).sendKeys("Subrata ");
 Thread.sleep(3000);
 driver.findElement(By.id("lname")).sendKeys("Das");
 Thread.sleep(3000);
 driver.findElement(By.id("username")).sendKeys("SD123");
 Thread.sleep(3000);
 driver.findElement(By.id("age")).sendKeys("22");
 Thread.sleep(3000);
 driver.findElement(By.id("mobile")).sendKeys("01761147512");
 Thread.sleep(3000);
 driver.findElement(By.id("email")).sendKeys("sumib2k17@gmail.com");
 Thread.sleep(3000);
 driver.findElement(By.id("password")).sendKeys("Sumib2k17@");
 Thread.sleep(3000);
 driver.findElement(By.className("registerbtn")).click(); 
 driver.get("http://localhost/Web_Project_Fall-main/Web_Project_Fall_main/completeProjectUser3/view/login.php");
 driver.manage().window().maximize();
 driver.findElement(By.id("username")).sendKeys("SD123");
 Thread.sleep(3000);
 driver.findElement(By.id("password")).sendKeys("Sumib2k17@");
 Thread.sleep(3000);
 driver.findElement(By.className("submit")).click();
 Thread.sleep(3000);
 driver.close();
}
}
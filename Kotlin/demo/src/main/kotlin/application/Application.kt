package application

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.context.annotation.ComponentScan

@SpringBootApplication
@ComponentScan(basePackages = ["controller", "entity"])
class Application

fun main(args: Array<String>) {
    SpringApplication.run(Application::class.java, *args)
}
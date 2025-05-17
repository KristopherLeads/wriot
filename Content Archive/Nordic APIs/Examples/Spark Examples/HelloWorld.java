// Example used in https://nordicapis.com/using-spark-to-create-apis-in-scala/

import static spark.Spark.*;

public class HelloWorld {
	public static void main(String[] args) {
    	get("/hello", (request, response) -> "Hello World");
	}
}

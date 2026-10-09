package controllers;

import play.mvc.*;

public class HelloWorldController extends Controller {
    
    public Result sayHello() {
        return ok("Hello, World!");
    }
}
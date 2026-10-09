package controllers;

import org.junit.Test;
import play.mvc.*;
import play.test.*;
import play.libs.Json;
import static play.test.Helpers.*;
import static org.junit.Assert.*;

public class HelloWorldControllerSpec {

    @Test
    public void testSayHello() {
        running(testServer(3333), () -> {
            Result result = route(fakeRequest(GET, "/hello"));
            assertEquals(200, result.status());
            assertEquals("Hello, World!", contentAsString(result));
        });
    }
}
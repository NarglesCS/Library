package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	//Example JSON constructor
	requestBody, err := json.Marshal(map[string]string{
		"Name":       "Nargles",
		"brogrammer": "YEAH BRO!",
	})

	//http.Post request, and response handling of packet header, body, trailer
	//Note: can use NewBufferString for a quick string
	resp, err := http.Post("https://postman-echo.com/post", "text/plain", bytes.NewBuffer(requestBody))
	if err == nil {
		head := resp.Header
		if err == nil {
			//Header is of type MAP with keys:
			keys := make([]string, 0, len(head))
			fmt.Println("Packet header keys")
			for k := range head {
				keys = append(keys, k)
			}
			for i := range keys {
				fmt.Print(keys[i], "\n")
			}

		}
		defer resp.Body.Close()

		//response is in the form of a packet. This gives us a memory location for the response.
		body, err := ioutil.ReadAll(resp.Body)
		if err == nil {
			//After ioutil, the characters are in ascii values. stirng(body) converts to a printable, readable string.
			body := string(body)
			fmt.Println("Packet Body")
			fmt.Print(body, "\n")
		}
		//Tail of the response
		tail := resp.Trailer
		fmt.Println("Packet trailer")
		fmt.Print(tail)
	}
}


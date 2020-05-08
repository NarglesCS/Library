package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
)

func main() {
	//http.PostForm request, and response handling of packet header, body, trailer
	//Note: can use NewBufferString for a quick string
	formData := url.Values{
		"Name":       {" Nargles"},
		"Profession": {" Professional CSGO Player"},
	}

	resp, err := http.PostForm("https://postman-echo.com/post", formData)
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
				fmt.Print(keys[i], "")
			}

		}
		// Code for converting the response body to JSON
		var result map[string]interface{}
		json.NewDecoder(resp.Body).Decode(&result)
		fmt.Println("\nPacket body")
		fmt.Println(result["form"])

		//Tail of the response
		tail := resp.Trailer
		fmt.Println("Packet trailer")
		fmt.Print(tail)
	}
}

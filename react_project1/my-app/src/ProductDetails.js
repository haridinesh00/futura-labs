import React from "react";
import { Card, Row } from "react-bootstrap";

function ProductDetails() {
  const obj = [
    {
      Name: "Google Pixel 6a",
      OS: "Android",
      Size: "6.7inch",
      Camera: "64MP",
      Price: 32000,
      ReleaseDate: "12-12-22",
      image: "https://m.media-amazon.com/images/I/61PW24157AL._AC_UF894,1000_QL80_.jpg"
    },
    {
      Name: "Google Pixel 7a",
      OS: "Android",
      Size: "6.7inch",
      Camera: "64MP",
      Price: 38000,
      ReleaseDate: "23-8-23",
      image: "https://www.ubuy.co.in/productimg/?image=aHR0cHM6Ly9pbWFnZXMtY2RuLnVidXkuY28uaW4vNjM0ZTNmYzkxNGJlMmQ0YTRiNmQ5OWYyLWdvb2dsZS1waXhlbC03LTVnLWFuZHJvaWQtcGhvbmUuanBn.jpg"
    },
    {
        Name: "Google Pixel 7",
        OS: "Android",
        Size: "6.8inch",
        Camera: "108MP",
        Price: 45000,
        ReleaseDate: "23-4-23",
        Description: "The Pixel 7 comes with 6.3-inch OLED display with 90Hz refresh rate and Google Tensor G2 processor. Specs also include 4355mAh battery, Dual camera on the back with 50MP main sensor and 10.8MP front selfie camera. ",
        image: "https://m.media-amazon.com/images/I/61U-Bid4WYL.jpg"
      },
      {
        Name: "Google Pixel 7",
        OS: "Android",
        Size: "6.8inch",
        Camera: "108MP",
        Price: 45000,
        ReleaseDate: "23-4-23",
        Description: "The Pixel 7 comes with 6.3-inch OLED display with 90Hz refresh rate and Google Tensor G2 processor. Specs also include 4355mAh battery, Dual camera on the back with 50MP main sensor and 10.8MP front selfie camera. ",
        image: "https://m.media-amazon.com/images/I/61U-Bid4WYL.jpg"
      },
      {
        Name: "Google Pixel 7",
        OS: "Android",
        Size: "6.8inch",
        Camera: "108MP",
        Price: 45000,
        ReleaseDate: "23-4-23",
        Description: "The Pixel 7 comes with 6.3-inch OLED display with 90Hz refresh rate and Google Tensor G2 processor. Specs also include 4355mAh battery, Dual camera on the back with 50MP main sensor and 10.8MP front selfie camera. ",
        image: "https://m.media-amazon.com/images/I/61U-Bid4WYL.jpg"
      },
      {
        Name: "Google Pixel 7",
        OS: "Android",
        Size: "6.8inch",
        Camera: "108MP",
        Price: 45000,
        ReleaseDate: "23-4-23",
        Description: "The Pixel 7 comes with 6.3-inch OLED display with 90Hz refresh rate and Google Tensor G2 processor. Specs also include 4355mAh battery, Dual camera on the back with 50MP main sensor and 10.8MP front selfie camera. ",
        image: "https://m.media-amazon.com/images/I/61U-Bid4WYL.jpg"
      },
      {
        Name: "Google Pixel 7",
        OS: "Android",
        Size: "6.8inch",
        Camera: "108MP",
        Price: 45000,
        ReleaseDate: "23-4-23",
        Description: "The Pixel 7 comes with 6.3-inch OLED display with 90Hz refresh rate and Google Tensor G2 processor. Specs also include 4355mAh battery, Dual camera on the back with 50MP main sensor and 10.8MP front selfie camera. ",
        image: "https://m.media-amazon.com/images/I/61U-Bid4WYL.jpg"
      },
      {
        Name: "Google Pixel 7",
        OS: "Android",
        Size: "6.8inch",
        Camera: "108MP",
        Price: 45000,
        ReleaseDate: "23-4-23",
        Description: "The Pixel 7 comes with 6.3-inch OLED display with 90Hz refresh rate and Google Tensor G2 processor. Specs also include 4355mAh battery, Dual camera on the back with 50MP main sensor and 10.8MP front selfie camera. ",
        image: "https://m.media-amazon.com/images/I/61U-Bid4WYL.jpg"
      }
  ];
  return (
    // <div xs={1} md={2} className="g-4" style={{ marginLeft: "5rem", marginTop: "5rem", display: 'flex', flexDirection: 'row' }}>
    <Row xs={1} md={2} className="g-4" style={{margin: "1vh"}}>
      {obj.map((i) => {
        return (
          <Card style={{ width: "16rem", borderRadius: "5px", display: 'flex', flexDirection: 'column', marginRight: "2rem"}}>
            <Card.Img
              variant="top"
              src={i.image}
            />
            <Card.Body>
              <Card.Title>{i.Name}</Card.Title>
              <Card.Text>
                OS: {i.OS}
                <br />
                Size: {i.Size}
                <br />
                Camera : {i.Camera}
                <br />
                ReleaseDate : {i.ReleaseDate}
              </Card.Text>
            </Card.Body>
          </Card>
        );
      })}
    </Row>
  );
}

export default ProductDetails;

import React from "react";
import * as BootStrap from "react-bootstrap";

const Header = () => {
  return (
    <BootStrap.Navbar bg="danger" expand="lg">
      <BootStrap.Container>
        <BootStrap.Navbar.Brand href="#home">
          Around the Block
        </BootStrap.Navbar.Brand>
        <BootStrap.Navbar.Toggle aria-controls="basic-navbar-nav" />
        <BootStrap.Navbar.Collapse id="basic-navbar-nav">
          <BootStrap.Nav className="me-auto">
            <BootStrap.Nav.Link href="#home">Home</BootStrap.Nav.Link>
            <BootStrap.Nav.Link href="#link">Link</BootStrap.Nav.Link>
            <BootStrap.NavDropdown title="Dropdown" id="basic-nav-dropdown">
              <BootStrap.NavDropdown.Item href="#action/3.1">
                Action
              </BootStrap.NavDropdown.Item>
              <BootStrap.NavDropdown.Item href="#action/3.2">
                Another action
              </BootStrap.NavDropdown.Item>
              <BootStrap.NavDropdown.Item href="#action/3.3">
                Something
              </BootStrap.NavDropdown.Item>
              <BootStrap.NavDropdown.Item href="#action/3.4">
                <BootStrap.NavDropdown.Divider />
                Separated link
              </BootStrap.NavDropdown.Item>
            </BootStrap.NavDropdown>
          </BootStrap.Nav>
        </BootStrap.Navbar.Collapse>
      </BootStrap.Container>
    </BootStrap.Navbar>
  );
};

export default Header;

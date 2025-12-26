from dataclasses import dataclass


@dataclass
class LoginDTO:
    username: str
    password: str


@dataclass
class LoginResponseDTO:
    token: str

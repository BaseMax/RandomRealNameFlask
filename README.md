# Random Real Name in Python Flask

A Python web-based application for generating random user-names (gender-aware), An online and secure service to create unique random usernames lists.

## Assignment

In most projects, we need to generate random names, but we do not want to use random characters. We need real names.

We have an email provider which provides your email address. By getting this repository they will be able to generate many random email address but meanfull names.

**The challenge of this is to generate a meaningful but UNIQUE name!**

Suppose you are going to generate 10k email address, so you need to have a lot of unique names. An email address is a mix of name, family, age, or maybe a date.
So by using different value we are going to generate unique name.

### Communication way

We are going to use **HTML**.

### Technology

Python, Flask

## Usage

In the first step you can use GET method and get in response this README page:

- `GET /`
- `127.0.0.1:5000/`

If you want to create a new random name use this route:

- `127.0.0.1:5000/get`

And if you want more than one after this route determine the number of names:

- `127.0.0.1:5000/get/<amount>`

By default this route generate both male and female names but if you want to specify gender, after this route write gender(male OR female):

- `127.0.0.1:5000/get/<amount>/<gender(male/female)>`

### The main part

When a request asks us to generate 1000 UNIQUE names. we need to make sure we are going to generate UNIQUE names.

In the process, Maybe we generate 2000 names and after filtering the final result was 1000 UNIQUE names. So when we find a `limit` number of unique names. it ends and we send the output to that request.

### Routes

- `GET /`

A route that will show this document and everyone can study more about the project as well as this README.markdown.

- `GET /get`

**Parameters:**

- The default value of `limit` is 1 but you are able to change limit to any number of emails you need. like 100.

- The default value of `gender` is `"both"`, But if you want to get random names for Male or Female you need to set it to `male` or `female`.

This route not going to generate an email for you. this only generates random and UNIQUE names.

**Output:**

```json
{
  "status": 1,
  "name": "alireza2000"
}
```

Or maybe as following if you are asking for more than one name:

```json
{
  "status": 1,
  "names": ["alireza2004", "hamid.h3000", "max.base1"]
}
```

Or if something went wrong:

```json
{
  "status": 0,
  "message": "Oops, sorry. Something does not go as we expected."
}
```

**Note:** Obviously, the HTTP Code is expected to be 200 if the request is answered successfully. Otherwise, you can use the appropriate code according to the error.

## What do you need to search for?

We need a long list of first names and last names.
There are several public databases about names.

It can be two different files too. One for first name and the second for family name.

## Database or not?

As it is clear, maybe there is no reason to use database in this project. But you can use the database you like.

You can also use the file to store names and surnames.
But keep in mind that your web service must be able to respond to a large number of simultaneous requests.

## Why Assignment?

Note, I have never applied for a job anywhere until now and this assignment project is designed by myself. Right now I'm enjoying GitHub and I'm not looking for solving assignments for others. Best Wishes.

## Authors

- Ahmadi
- Max Base

Anyone is welcome to contribute, change or develop this project. Thanks in advance, Any comments are appreciated.

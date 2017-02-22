# Python-Twitter-Program
Having access to the Twitter API can help you manage your social media accounts, and allow you to mine social media for data. This can be useful for brand promotion if you represent a business or an organization, and it can be enjoyable and entertaining for individual users and hobbyist programmers.
Introduction

Having access to the Twitter API can help you manage your social media accounts, and allow you to mine social media for data. This can be useful for brand promotion if you represent a business or an organization, and it can be enjoyable and entertaining for individual users and hobbyist programmers.

In this article, we will outline the steps necessary for you to create a Twitter application.

We’ll then build a script in Python that uses the Tweepy library to make use of the Twitter API.

Prerequisites

Before you begin, ensure you have the following prerequisites in place:

A Twitter account with a valid phone number, which you can add via the Mobile section of your Settings when you’re logged in
A Python programming environment set up; this can either be on your local machine or on a server
Step 1 — Create Your Twitter Application
Let’s go through the process of creating a Twitter application and retrieving your API access keys and tokens. These tokens are what will allow you to authenticate any applications you develop that work with Twitter. As mentioned in the prerequisites, you’ll need a valid phone number in order to create applications using Twitter.

Open up your browser and visit https://apps.twitter.com/ then log in using your Twitter account credentials. Once logged in, click the button labeled Create New App.

Create New Twitter App

You will now be redirected to the application creation page.

Fill out Twitter application details

On this page, you’ll fill out the required fields.

Note: The name that you provide for your app must be unique to your particular app. You cannot use the name as shown here since it already exists. 

Name: DigitalSeaBot-example-app
Description: My example application.
Website: https://my.example.placeholder
Read the Twitter Developer Agreement. If you agree to continue at this point, click the checkbox next to the line that reads, Yes, I have read and agree to the Twitter Developer Agreement.

Once you click the Create your Twitter application button at the bottom of the page, you’ll receive a confirmation page.

Twitter application creation confirmation page

After successfully creating your application, you will be redirected to your application's Details page, which provides you with some general information about your app.

Step 2 — Modify Your Application’s Permission Level and Generate Your Access Tokens
From the Details page, let’s navigate over to the Permissions page to ensure that we have the appropriate access level to generate our application keys.

By default, your Twitter app should have Read and Write access. If this is not the case, modify your app to ensure that you have Read and Write access. This will allow your application to post on your behalf.

Twitter application permissions

After updating your application’s permissions to allow posting, click the tab labeled Keys and Access Tokens. This will take you to a page that lists your Consumer Key and Consumer Secret, and also will allow you to generate your Access Token and Access Token Secret. These are necessary to authenticate our client application with Twitter.

Click the button labeled Create my access token under the Access Token heading to generate your Access Token and Access Token Secret.

Twitter access token creation

Now you will now have an Access Token and an Access Token Secret.

Twitter application settings

On the page you’re redirected to, you'll also see the application’s Access Level, your username as the Owner, and your Owner ID.

"use strict";
const nodemailer = require("nodemailer");

function main(){

  /*

  let testAccount = nodemailer.createTestAccount();

  let transporter = nodemailer.createTransport({
    host: "smtp.ethereal.email",
    port: 587,
    secure: false, // true for 465, false for other ports
    auth: {
      user: testAccount.user, // generated ethereal user
      pass: testAccount.pass // generated ethereal password
    }
  });

  */

  let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: '',
      pass: ''
    }
  });

  let info = transporter.sendMail({
    from: '"German" <@gmail.com>', // sender address
    to: "", // list of receivers
    subject: "Email Verification", // Subject line
    text: "To complete your register follow this link" // plain text body
    //html: "<b>Hello world?</b>" // html body
  });

  console.log("Message sent: %s", info.messageId);

  console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info));

}

main();

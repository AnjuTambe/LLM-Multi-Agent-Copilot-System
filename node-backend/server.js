require('dotenv').config();
const express = require('express');
const cors = require('cors');
const sgMail = require('@sendgrid/mail');

const app = express();
app.use(cors());
app.use(express.json());

// ✅ Use API key from environment variable
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

// 📩 Dynamic email route
app.post('/send-email', async (req, res) => {
  const { to, subject, name, message } = req.body;

  const email = {
    to: to, // recipient email
    from: 'tambeanju987@gmail.com', // ✅ must be your verified sender email
    subject: subject,
    html: `
      <h2>Hello ${name},</h2>
      <p>${message}</p>
      <p>— Multi-Agent Copilot</p>
    `,
  };

  try {
    await sgMail.send(email);
    res.status(200).json({ success: true, message: 'Email sent successfully!' });
  } catch (error) {
    console.error(error.response?.body || error);
    res.status(500).json({ success: false, message: 'Email failed to send.' });
  }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

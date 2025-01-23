// src/api/auth.js
import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000";

export const Register = async (formData) => {
  try {
    const response = await axios.post(`${BASE_URL}/auth/register/`, formData, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return response.data;
  } catch (error) {
    throw error.response;
  }
};

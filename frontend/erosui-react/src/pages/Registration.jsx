// src/pages/SignUp.jsx
import React, { useState } from "react";
import { Register } from "../api/auth";
import InputField from "../components/common/inputField";
import Header from "../components/common/Header";

const Registration = () => {
  const [formData, setFormData] = useState({
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    pass_cfm: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await Register(formData);
      console.log("Sign-up successful:", data);
      // Optionally, redirect the user or display a success message
    } catch (error) {
      console.error("Sign-up error:", error);
    }
  };

  return (
    <>
      <Header />
      <div className="w-full bg-light lg:px-32 md:px-[5.5rem] py-[4.99rem] px-7 font-dmSans">
        <h1 className="text-2xl text-black">Create Account</h1>
        <p className="text-gray font-small mt-3">
          Already have an account?{" "}
          <span className="text-black font-outfit">Log in here</span>
        </p>

        <div className="w-full lg:flex block gap-5 mt-14">
          <div className="w-full">
            <InputField
              type="email"
              name="email"
              onChange={handleChange}
              label="E-mail"
            />

            <InputField
              type="text"
              name="first_name"
              onChange={handleChange}
              label="First Name"
            />

            <InputField
              type="password"
              name="password"
              onChange={handleChange}
              label="Password"
            />
          </div>

          <div className="w-full">
            <InputField
              type="text"
              name="title"
              onChange={handleChange}
              label="Title"
              placeholder="Select your title"
            />

            <InputField
              type="text"
              name="last_name"
              onChange={handleChange}
              label="Last Name"
            />

            <InputField
              type="password"
              name="pass_cfm"
              onChange={handleChange}
              label="Confirm Password"
            />
          </div>
        </div>

        <button
          onClick={handleSubmit}
          className="bg-black rounded-full px-32 py-[14px] font-outfit text-light font-[500] text-[15px] border border-black hover:text-black hover:bg-light transition-all"
        >
          Continue
        </button>
      </div>
    </>
  );
};

export default Registration;

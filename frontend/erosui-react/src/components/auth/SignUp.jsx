import React, { useState } from "react";
import axios from "axios";

const SignUp = () => {
  const [formData, setFormData] = useState({
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    pass_cfm: "",
  });
  // const [message, setMessage] = useState("");
  // const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    axios
      .post("http://127.0.0.1:5000/auth/sign_up/", formData, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((resp) => console.log(resp.data))
      .catch((err) => console.log(err.response));
  };

  return (
    <div className="w-full bg-light lg:rounded-l-3xl lg:px-32 md:px-[5.5rem] py-[4.99rem] px-7 font-dmSans">
      <h1 className="text-4xl font-medium text-black">Create Account</h1>

      <div className="lg:flex block gap-5 mt-14">
        <div className="lg:w-1/2 relative group focus-within:text-primaryDark">
          <label className="absolute bg-light px-[8px] text-gray text-[15px] font-[400] translate-x-[30px] -translate-y-1/2 transition-all group-focus-within:text-primaryDark">
            First Name
          </label>
          <input
            type="text"
            name="first_name"
            onChange={handleChange}
            className="w-full focus:outline-none focus:border-primaryDark bg-transparent border border-gray rounded-[8px] py-[14.5px] px-4"
          />
        </div>

        <div className="lg:w-1/2 lg:mt-0 mt-8 relative group focus-within:text-primaryDark">
          <label className="absolute bg-light px-[8px] text-gray text-[15px] font-[400] translate-x-[30px] -translate-y-1/2 transition-all group-focus-within:text-primaryDark">
            Last Name
          </label>
          <input
            type="text"
            name="last_name"
            onChange={handleChange}
            className="w-full focus:outline-none focus:border-primaryDark bg-transparent border border-gray rounded-[8px] py-[14.5px] px-4"
          />
        </div>
      </div>

      <div className="w-full relative mt-8 group focus-within:text-primaryDark">
        <label className="absolute bg-light px-[8px] text-gray text-[15px] font-[400] translate-x-[30px] -translate-y-1/2 transition-all group-focus-within:text-primaryDark">
          E-mail
        </label>
        <input
          type="email"
          name="email"
          onChange={handleChange}
          className="w-full focus:outline-none focus:border-primaryDark bg-transparent border border-gray rounded-[8px] py-[14.5px] px-4"
        />
      </div>

      <div className="lg:flex block gap-5 mt-8">
        <div className="lg:w-1/2 relative group focus-within:text-primaryDark">
          <label className="absolute bg-light px-[8px] text-gray text-[15px] font-[400] translate-x-[30px] -translate-y-1/2 transition-all group-focus-within:text-primaryDark">
            Password
          </label>
          <input
            type="password"
            name="password"
            onChange={handleChange}
            className="w-full focus:outline-none focus:border-primaryDark bg-transparent border border-gray rounded-[8px] py-[14.5px] px-4"
          />
        </div>

        <div className="lg:w-1/2 lg:mt-0 mt-8 relative group focus-within:text-primaryDark">
          <label className="absolute bg-light px-[8px] text-gray text-[15px] font-[400] translate-x-[30px] -translate-y-1/2 transition-all group-focus-within:text-primaryDark">
            Confirm Password
          </label>
          <input
            type="password"
            name="pass_cfm"
            onChange={handleChange}
            className="w-full focus:outline-none focus:border-primaryDark bg-transparent border border-gray rounded-[8px] py-[14.5px] px-4"
          />
        </div>
      </div>

      <button
        onClick={handleSubmit}
        className="w-full mt-8 bg-primaryDark rounded-[8px] p-[11px] font-outfit text-light font-[600] text-[21px]"
      >
        Sign Up
      </button>

      <p className="text-gray font-medium mt-5">
        Already have an account?{" "}
        <span className="text-primaryDark font-outfit">Sign In</span>
      </p>
    </div>
  );
};

export default SignUp;

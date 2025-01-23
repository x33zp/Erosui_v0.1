import React, { useState, useEffect } from "react";
import axios from "axios";

const Profile = (props) => {
  const [userName, setUserName] = useState("");
  // const [message, setMessage] = useState("");
  // const [error, setError] = useState("");

  useEffect(() => {
    const fetchUserName = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:5000/protected/profile/",
          {
            headers: { Authorization: `Bearer ${props.token}` },
          }
        );
        response.data.access_token &&
          props.setToken(response.data.access_token);
        setUserName(response.data.email);
      } catch (error) {
        console.error("Error fetching profile:", error);
        props.removeToken();
      }
    };

    fetchUserName();
  }, [props.token]);

  return <div>Welcome: {userName}</div>;
};

export default Profile;

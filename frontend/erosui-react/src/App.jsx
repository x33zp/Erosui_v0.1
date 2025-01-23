import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Registration from "./pages/Registration";
import SignIn from "./components/auth/SignIn";
import FormArt from "./components/auth/FormArt";
import Profile from "./components/Profile";
import useToken from "./api/AuthProvider";
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'

function App() {
  const { token, removeToken, setToken } = useToken();

  return (
    <Router>
      <>
        {/* <FormArt /> */}
        <Registration />
        {!token && token !== "" && token !== undefined ? (
          <Routes>
            <Route
              path="/profile"
              element={<Navigate to="/sign_in" replace />}
            />
            <Route
              path="/sign_in"
              element={<SignIn setToken={setToken} />}
            ></Route>
          </Routes>
        ) : (
          <>
            <Routes>
              <Route
                path="account/sign_in"
                element={<Navigate to="/profile" replace />}
              />
              <Route
                exact
                path="/profile"
                element={
                  <Profile
                    token={token}
                    setToken={setToken}
                    removeToken={removeToken}
                  />
                }
              ></Route>
            </Routes>
          </>
        )}
        {/* <Profile /> */}
      </>
    </Router>
  );
}

export default App;

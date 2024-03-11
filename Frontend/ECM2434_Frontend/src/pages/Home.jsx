import React, { useEffect, useState } from "react";
import { useUser } from "../contexts/userContext";
import { CreateQuestForm } from "../components/forms/createQuest/createQuestForm";
import { DailyQuest } from "../components/dailyQuest";
import classes from "./Home.module.css";
import { useNavigate } from "react-router-dom";
// import { DailyQuestPage } from "./DailyQuestPage";
import Button from "@mui/material/Button"

const Home = () => {
  const { user } = useUser();
  const [showForm, setShowForm] = useState(false);
  const [showDailyQuest, setShowDailyQuest] = useState(false);

  const navigate = useNavigate();

  //This useEffect is used to check if the user is logged in, if they are then they are redirected to the daily quest page
  useEffect(() => {
    if (user) {
      console.log("User is logged in");
      navigate("/dailyQuest");
    }
  }, [user]);
  //This return is conditionally rendered based on whether the user is logged in or not
  return (
    <>

      <div className={classes.container}>
        <div className={classes.leftSideContent}>
          <h1>
            Daily <span className={classes.ecoGradient}>Eco</span> Quest
          </h1>
          <div className={classes.textGroup}>
            <h5>Challenge your friends at Uni,</h5>
            <h5>Save the planet.</h5>
          </div>
          <div className={classes.buttonGroup}>
            <button
              className={classes.createQuestButton}
              onClick={() => setShowForm(!showForm)}
            >
              Create Quest
            </button>
            <button
              className={classes.dailyQuestButton}
              onClick={() => setShowDailyQuest(!showDailyQuest)}
            >
              Daily Quest
            </button>
          </div>
        </div>
        {showForm && <CreateQuestForm />}
        {showDailyQuest && <DailyQuest />}
      </div>

    </>
  );
};

export default Home;

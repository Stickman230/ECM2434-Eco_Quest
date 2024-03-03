import React from "react";
import classes from "./submitQuestForm.module.css";
import { useUser } from "../../../contexts/userContext";
import { useDropzone } from 'react-dropzone'
import { ImageSubmit } from "../../imageSubmit";
import ApiClient from "../../../api/index";
//Created by Cufe12345(Callum Young)
export function SubmitQuestForm({ onBackClick, setOpen,setPopupText,quest }) {
  const { user, userData } = useUser();

  //Stores the file
  const [file, setFile] = React.useState(null);

  //Handles the file drop
  const { acceptedFiles, getRootProps, getInputProps } = useDropzone({
    onDrop: acceptedFiles => {
      console.log(acceptedFiles);
      setFile(acceptedFiles[0]);
    }
  });
  /**
   * This function submits the quest
   */
  async function submitQuest() {
    console.log("Submitting quest");
    let dataImg = {
      name: file.name,
      description: "n/a for now",
    };
    let imgURL = null;
    let errorOccured = false;
    await ApiClient.api
      .uploadImage(user, dataImg, file)
      .then((res) => {
        imgURL = res?.image;
        console.log(res);
      })
      .catch((error) => {
        console.warn(error);
      });
      if(imgURL === null){
        console.log("Failed to submit quest, no image");
        setPopupText("Failed to submit quest");
        setOpen(true);
        errorOccured = true;
      }
    //submit on backend and pass imgURL and if successful
    let data = {
      questID: quest.questID,
      user:userData.id,
      imgURL: imgURL,
      info: "n/a for now",
      verified: false,
    };
    await ApiClient.api
      .questSubmission(user, data)
      .then((res) => {
        console.log(res);
      })
      .catch((error) => {
        console.warn(error);
        console.log("Failed to submit quest");
        setPopupText("Failed to submit quest, please try again");
        setOpen(true);
        errorOccured = true;
      });
    if(!errorOccured){
      console.log("Quest Submitted");
      setPopupText("Quest Submitted, when verified you will receive points");
      setOpen(true);
    }
    //Redirect to Feed
  }

  return (
    <div className={classes.card}>
      <div className={classes.backContainer}>
        <button onClick={onBackClick} className={classes.backButton}>
          <p>Back</p>
        </button>
      </div>
      <h1>Submit Quest</h1>
      <p>Attach an image of completed quest below</p>
      {file ? (
        <div className={classes.imgContainer}>

          <img src={URL.createObjectURL(file)} alt="Quest" className={classes.imgPreview} />
        </div>
      ) : (
        <div {...getRootProps()} className={classes.dropzone}>
          <input {...getInputProps()} />
          <p className={classes.dropzoneText1}>Drag & drop images here or Browse</p>
          <p className={classes.dropzoneText2}>Accepted file types: .png, .jpg, .jpeg</p>
        </div>
      )}
      <ImageSubmit setImage={setFile} img={file} />
      <button onClick={submitQuest} className={classes.submitButton}>
        Submit
      </button>
    </div>
  );
}

import React, { useState } from 'react';
import axios from 'axios';
import Webcam from 'react-webcam';

const WebcamCapture = ({ email, submitName }) => {
  const webcamRef = React.useRef(null);
  const videoConstraints = {
    width: 200,
    height: 200,
    facingMode: 'user'
  };
  const [name, setName] = useState('')
  const capture = React.useCallback(
    (status) => {
      const imageSrc = webcamRef.current.getScreenshot();
      console.log(`imageSrc = ${imageSrc}`)
      //for deployment, you should put your backend url / api
      axios.post('http://127.0.0.1:5000/api', { data: imageSrc, status: status})
        .then(res => {
          console.log(`response = ${res.data}`)
          setName(res.data)
          alert(res.data)
        })
        .catch(error => {
          console.log(`error = ${error}`)
        })
    },
    [webcamRef]
  );

  const captureNewEntry = React.useCallback(
    () => {
      const imageSrc = webcamRef.current.getScreenshot();
      console.log({ data: imageSrc, name: email })
      //for deployment, you should put your backend url / api
      axios.post('http://127.0.0.1:5000/register', { data: imageSrc, name: email })
        .then(res => {
          console.log(`response = ${res.data}`)
          setName(res.data)
          alert(res.data)
        })
        .catch(error => {
          console.log(`error = ${error}`)
        })
    },
    [webcamRef, email]
  );

  return (
    <div style={{ textAlign: "center" }}>
      <Webcam
        audio={false}
        height={600}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={600}
        videoConstraints={videoConstraints}
        style={{ border: "solid 8px #70e3cf", borderRadius: '24px' }}
      />
      <div>
        {submitName && <button
          className="-mt-px inline-flex cursor-pointer justify-center whitespace-nowrap rounded-sm border-0 bg-gradient-to-r from-secondary-500 to-secondary-400 py-4 px-7 text-center font-medium leading-4 text-white no-underline shadow-lg"
          onClick={captureNewEntry}
          style={{ marginTop: '10px', borderRadius: '7px' }}
        >Register</button>
        }
        {
          !submitName &&
          <>
            <button
              className="-mt-px inline-flex cursor-pointer justify-center whitespace-nowrap rounded-sm border-0 bg-gradient-to-r from-secondary-500 to-secondary-400 py-4 px-7 text-center font-medium leading-4 text-white no-underline shadow-lg"
              onClick={()=>capture("login")}
              style={{ marginTop: '10px', borderRadius: '7px' }}
            >Login</button>
            <button
              className="-mt-px ml-28 inline-flex cursor-pointer justify-center whitespace-nowrap rounded-sm border-0 bg-gradient-to-r from-secondary-500 to-secondary-400 py-4 px-7 text-center font-medium leading-4 text-white no-underline shadow-lg"
              onClick={()=>capture("logout")}
              style={{ marginTop: '10px', borderRadius: '7px' }}
            >Logout</button>
          </>
        }
      </div>
      {/* <h2>{name}</h2> */}
    </div>
  );

};

export default WebcamCapture;
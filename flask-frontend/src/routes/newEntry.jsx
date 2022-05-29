import React from 'react'

import { Layout } from '../components/layout'
import { Hero } from '../components/hero'
import { HeroIllustration } from '../components/hero-illustration'

export default function NewEntry() {
  return (
    <Layout>
      <Hero
        instructions={
          <ul>
            <li>This page is to Register New Entry</li>
            <li>To Register yourself, Write your Roll number in the box given below</li>
            <li>Then look properly in the camera, and click <b>Register</b></li>
            <li>Click on <b>Back to Home</b></li>
          </ul>
        }
        submitName = {true}
        btnName="Register"
        redirectTo="./"
        redirectBtn="Back to Home"
        // illustration={<HeroIllustration />}
      />
    </Layout>
  )
}

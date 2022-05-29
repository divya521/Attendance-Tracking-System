import React from 'react'

import { Layout } from '../components/layout'
import { Hero } from '../components/hero'
import { HeroIllustration } from '../components/hero-illustration'

export default function HomePage() {
  return (
    <Layout>
      <Hero
        instructions={
          <ul>
            <li>This page is to mark your attendance</li>
            <li>If you are not registered yet first go to the registration page and register yourself by clicking the <b>Register New Entry</b> button below</li>
            <li>To login click on <b>login</b> and to log out click on <b>logout</b> button </li>
          </ul>
        }
        btnName="Submit"
        redirectTo="./newEntry"
        redirectBtn="Register New Entry"
        // illustration={<HeroIllustration />}
      />
    </Layout>
  )
}

import React from 'react';
import { Helmet as HelmetComponent } from 'react-helmet';

const Helmet = () => (
  <HelmetComponent defaultTitle="Renova" titleTemplate="%s &bull; Renova" />
);

export default Helmet;

import React from 'react';
import PropTypes from 'prop-types';

import styled from 'styled-components';

import { Footer } from 'components/Common';
import { Header, Navigation } from 'components/Dashboard';

const propTypes = {
  children: PropTypes.node.isRequired
};

const Layout = props => (
  <Page>
    <Header />
    <Navigation />
    <Content>
      <Container>{props.children}</Container>
    </Content>
    <Footer />
  </Page>
);

Layout.propTypes = propTypes;

const Page = styled.div`
  display: grid;
  grid-template-rows: auto auto 1fr auto;
  min-height: 100vh;
`;

export const Wrapper = styled.div`
  display: grid;
  grid-template-columns: auto 960px auto;
`;

export const Container = styled.div`
  grid-column: 2;
`;

const Content = styled(Wrapper)``;

export default Layout;

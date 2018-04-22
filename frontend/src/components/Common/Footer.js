import React from 'react';

import styled from 'styled-components';
import { Container, Wrapper } from 'layouts/Dashboard';

const Footer = () => (
  <FooterWrapper>
    <Container>
      &copy; 2018 Renova. A community gaming experience provided by{' '}
      <a href="http://avalonstar.tv">Avalonstar</a>. All images and content
      belong to their respective creators.
    </Container>
  </FooterWrapper>
);

const FooterWrapper = styled(Wrapper)`
  padding: 1.25rem 0;

  border-top: 1px solid #e4e6ec;
  color: #c5c8d9;
  font-size: 0.85rem;
`;

export default Footer;
